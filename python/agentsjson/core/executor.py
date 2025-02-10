import json
from typing import Any, Dict, List, Tuple, Union
import importlib
from agentsjson.integrations.types import ExecutorType
from benedict import benedict
import re
import sys
from collections.abc import Sized

from .models.bundle import Bundle
from .utils import convert_dot_digits_to_brackets
from .models.auth import AuthConfig, AuthType, OAuth1AuthConfig, UserPassCredentials, OAuth2AuthConfig
from .parsetools import ToolFormat
from .models.schema import Flow, Link

def apply_link(link: Link, execution_trace: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """
    Maps values between actions using benedict for robust dot notation support,
    including array indexing like line_items[0].quantity.
    """
    apply = benedict({
        "parameters": {},
        "requestBody": {},
        "responses": {}
    })

    # Get the field type data directly from the fieldPath
    source_trace = benedict(execution_trace[link.origin.actionId])
    field_path = convert_dot_digits_to_brackets(link.origin.fieldPath)
    
    field_path_parts = field_path.split('.')
    field_type = field_path_parts[0] if field_path_parts else None
            
    source_value = source_trace.get(field_path, None)
    
    # If the source value does not exist, do nothing
    if source_value is None:
        return dict(apply)

    # Apply the value to the target field
    target_path = convert_dot_digits_to_brackets(link.target.fieldPath)
    apply[target_path] = source_value
    return dict(apply)

def resolve_auth(auth: AuthConfig) -> Union[str, Tuple[str, str], OAuth1AuthConfig, OAuth2AuthConfig]:
    """
    Resolve the auth key from the auth config.
    """
    
    if auth.type == AuthType.OAUTH1 or auth.type == AuthType.OAUTH2:
        return auth
    elif auth.type == AuthType.API_KEY:
        return auth.key_value
    elif auth.type == AuthType.BEARER:
        return auth.token
    elif auth.type == AuthType.BASIC:
        credentials = auth.credentials
        if isinstance(credentials, UserPassCredentials):
            return credentials.username, credentials.password
        elif isinstance(credentials, str):
            return credentials
        else:
            raise ValueError(f"Unsupported auth credentials type: {type(credentials)}")

    else:
        raise ValueError(f"Unsupported auth type: {auth.type}")

def get_size(obj: Any) -> int:
    """
    Efficiently estimate the size of an object and its nested contents.
    """
    seen = set()  # Track objects to handle circular references
    
    def inner_size(obj: Any) -> int:
        obj_id = id(obj)
        if obj_id in seen:
            return 0
        seen.add(obj_id)
        
        size = sys.getsizeof(obj)
        
        if isinstance(obj, dict):
            size += sum(inner_size(k) + inner_size(v) for k, v in obj.items())
        elif isinstance(obj, (list, tuple, set)):
            size += sum(inner_size(i) for i in obj)
        
        return size
    
    return inner_size(obj)

def execute(bundle: Bundle, flow: Flow, auth: AuthConfig, parameters: Dict[str, Any], requestBody: Dict[str, Any], manageMemory: bool = False) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """
    Executes a flow of Actions in order, applying link-based parameter link.
    Each new link is deep-merged so we don't overwrite nested structures.
    
    Returns:
        Tuple containing two dictionaries:
        - First dict: Small responses (if manageMemory=True) or all responses (if manageMemory=False)
        - Second dict: Large responses (if manageMemory=True) or empty dict (if manageMemory=False)
    """
    
    if not flow.actions:
        return {}, {}
        
    # Initialize execution trace with flow parameters
    execution_trace = benedict({})
    execution_trace[flow.id] = {
        "parameters": parameters,
        "requestBody": requestBody,
        "responses": {}
    }
    
    # Execute each action in order
    for action in flow.actions:
        # Dynamically import the integration package
        integration_module = importlib.import_module(
            f".{action.sourceId}",
            package="agentsjson.integrations"
        )
        operation_map_type = integration_module.map_type # Describes the type of executor to use
        operation_map = integration_module.map
        operation = operation_map[action.operationId]
        
        # Find all links targeting this action
        action_links = []
        
        if flow.links:
            action_links = [
                m for m in flow.links 
                if m.target and m.target.actionId == action.id
            ]
                
        # Initialize action parameters
        action_parameters = benedict({})
        action_requestBody = benedict({})
        
        # Apply each link and merge the results
        for link in action_links:
            apply = apply_link(link, execution_trace)
        
            # Deep merge parameters and requestBody
            action_parameters.merge(apply.get("parameters", {}), overwrite=True)
            action_requestBody.merge(apply.get("requestBody", {}), overwrite=True)
                    
        # Convert benedict objects back to plain dicts
        action_parameters = dict(action_parameters)
        action_requestBody = dict(action_requestBody)

        # Store the parameters in execution trace
        execution_trace[action.id] = {
            "parameters": action_parameters,
            "requestBody": action_requestBody
        }
        
        # Get authentication
        auth_key = resolve_auth(auth)
        
        # Execute the operation
        if operation_map_type == ExecutorType.RESTAPIHANDLER:
            result = operation(auth, parameters=action_parameters, requestBody=action_requestBody)
        else:
            if isinstance(auth_key, tuple):
                result = operation(auth_key[0], auth_key[1], **action_parameters, **action_requestBody)
            else:
                result = operation(auth_key, **action_parameters, **action_requestBody)
        
        if "responses" not in execution_trace[action.id]:
            execution_trace[action.id]["responses"] = {}
        execution_trace[action.id]["responses"]["success"] = result

    def manage_memory(execution_trace: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        # Define size threshold (e.g., 10Kb)
        SIZE_THRESHOLD = 10
        
        small_responses = benedict({})
        large_responses = benedict({})
        
        # Split responses based on size
        for key, value in dict(execution_trace).items():
            # More efficient size calculation
            approx_size = get_size(value)
            
            if approx_size < SIZE_THRESHOLD:
                small_responses[key] = value
            else:
                large_responses[key] = value
                
        return dict(small_responses), dict(large_responses)
    
    # Process flow response links
    flow_response_links = []
    if flow.links:
        flow_response_links = [
            m for m in flow.links 
            if m.target and m.target.actionId == flow.id 
            and m.target.fieldPath.startswith("responses")
        ]
    
    if not flow_response_links:
        # If no response links defined, return the last action's response
        last_action = flow.actions[-1]
        if manageMemory:
            return manage_memory(execution_trace[last_action.id]["responses"])
        else:
            return execution_trace[last_action.id]["responses"], {}
    
    # Merge all flow response links
    flow_responses = benedict(execution_trace[flow.id]["responses"])
    for link in flow_response_links:
        apply = apply_link(link, execution_trace)
        if "responses" in apply:
            flow_responses.merge(apply["responses"], overwrite=True)

    if manageMemory:
        return manage_memory(flow_responses)
    else:
        return dict(flow_responses), {}


def execute_flows(response: Any, format: ToolFormat, bundle: Bundle, flows: List[Flow], auth: AuthConfig, manageMemory: bool = False) -> Dict[str, Any]:
    """
    Wrapper around `execute` that parses a tool call response to execute the flows.
    
    Returns a dictionary of flow ids and their results.
    """
    if format != ToolFormat.OPENAI:
        raise ValueError(f"Unsupported tool format: {format}")
        
    results = {}
    results_large = {}
    if not response.choices[0].message.tool_calls:
        return {"message": response.choices[0].message.content}
    
    for tool_call in response.choices[0].message.tool_calls:
        args_dict = json.loads(tool_call.function.arguments)

        # Account for missing "parameters" and "requestBody" keys
        flow = next(f for f in flows if f.id == tool_call.function.name)
        if "parameters" not in args_dict and "requestBody" not in args_dict:
            parameters = args_dict
            requestBody = {}
        elif "parameters" not in args_dict and "requestBody" in args_dict:
            parameters = {}
            requestBody = args_dict.get("requestBody", {})
        elif "parameters" in args_dict and "requestBody" not in args_dict:
            parameters = args_dict.get("parameters", {})
            requestBody = {}
        else:
            parameters = args_dict.get("parameters", {})
            requestBody = args_dict.get("requestBody", {})
        if manageMemory:
            small_results, large_results = execute(bundle=bundle, flow=flow, auth=auth, parameters=parameters, requestBody=requestBody, manageMemory=manageMemory)
            results[flow.id] = small_results
            results_large[flow.id] = large_results
        else:
            results[flow.id] = execute(bundle=bundle, flow=flow, auth=auth, parameters=parameters, requestBody=requestBody, manageMemory=manageMemory)

    return results, results_large

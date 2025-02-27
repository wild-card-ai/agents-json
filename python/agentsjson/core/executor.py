import json
from typing import Any, Dict, List, Optional, Tuple, Union
import importlib
from agentsjson.integrations.types import ExecutorType
from benedict import benedict
import re
from typing import TypeVar

from .models.bundle import Bundle
from .utils import convert_dot_digits_to_brackets
from .models.auth import AuthConfig, AuthType, OAuth1AuthConfig, UserPassCredentials, OAuth2AuthConfig
from .parsetools import ToolFormat
from .models.schema import AgentsJson, Flow, Link

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
    
    # Check from the end of the path until we find a value or reach the start
    field_path_parts = field_path.split('.')
    for i in range(len(field_path_parts) - 1, 0, -1):
        partial_path = '.'.join(field_path_parts[:i])
        # Skip if immediate parent is parameters or requestBody
        if field_path_parts[i-1] in ['parameters', 'requestBody']:
            continue
            
        intermediate_value = source_trace.get(partial_path, None)
        if intermediate_value is None or intermediate_value == "" or \
           (isinstance(intermediate_value, dict) and not intermediate_value) or \
           (isinstance(intermediate_value, list) and not intermediate_value):
            raise ValueError(f"Cannot access '{field_path}' because intermediate path '{partial_path}' is empty")
        # If we found a non-empty value, we can stop checking
        break
    
    
    
    # If we get here, the source value is None but the path is valid
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

def _execute(bundle: Optional[Bundle], flow: Flow, auth: AuthConfig, parameters: Dict[str, Any], requestBody: Dict[str, Any]) -> Dict[str, Any]:
    """
    Executes a flow of Actions in order, applying link-based parameter link.
    Each new link is deep-merged so we don't overwrite nested structures.
    """
    
    if not flow.actions:
        return {}
        
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
        return execution_trace[last_action.id]["responses"]
    
    # Merge all flow response links
    flow_responses = benedict(execution_trace[flow.id]["responses"])
    for link in flow_response_links:
        apply = apply_link(link, execution_trace)
        if "responses" in apply:
            flow_responses.merge(apply["responses"], overwrite=True)
    
    return dict(flow_responses)


def _parse_tool_call(args_dict: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    
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
        
    return parameters, requestBody

def execute_flows(response: Any, format: ToolFormat, bundle: Bundle, flows: List[Flow], auth: AuthConfig) -> Dict[str, Any]:
    """
    Wrapper around `execute` that parses a tool call response to execute the flows.
    Use when loading flows from an agents.json file.
    
    Returns a dictionary of flow ids and their results.
    """
    if format != ToolFormat.OPENAI:
        raise ValueError(f"Unsupported tool format: {format}")
        
    results = {}
        
    if not response.choices[0].message.tool_calls:
        return {"message": response.choices[0].message.content}
    
    for tool_call in response.choices[0].message.tool_calls:
        args_dict = json.loads(tool_call.function.arguments)
        parameters, requestBody = _parse_tool_call(args_dict)
        
        flow = next(f for f in flows if f.id == tool_call.function.name)    
        results[flow.id] = _execute(bundle=bundle, flow=flow, auth=auth, parameters=parameters, requestBody=requestBody)
    return results


def execute(agentsjson: AgentsJson, response: Any, format: ToolFormat, auth: AuthConfig) -> Dict[str, Any]:
    """
    Executes flows from a tool call response and returns the result.
    """
    results = {}

    if format != ToolFormat.OPENAI:
        raise ValueError(f"Unsupported tool format: {format}")
    
    if not response.choices[0].message.tool_calls:
        return {"message": response.choices[0].message.content}
    
    for tool_call in response.choices[0].message.tool_calls:
        args_dict = json.loads(tool_call.function.arguments)
        parameters, requestBody = _parse_tool_call(args_dict)
        
        flow = next(f for f in agentsjson.flows if f.id == tool_call.function.name)
        results[flow.id] = _execute(bundle=None, flow=flow, auth=auth, parameters=parameters, requestBody=requestBody)
    
    return results
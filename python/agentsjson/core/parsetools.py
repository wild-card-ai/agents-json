from enum import Enum
from typing import List, Dict, Any
from .models.tools import ToolFormat
from .models.schema import Flow
from .models.schema import AgentsJson

def get_tool_prompt(agentsjson: AgentsJson) -> str:
    """Get a prompt for the tools in the agentsjson"""
    return flows_prompt(agentsjson.flows)

def get_tools(agentsjson: AgentsJson, format: ToolFormat) -> List[Dict[str, Any]]:
    """Get tools for all flows in an agentsjson using a given format"""
    if format == ToolFormat.OPENAI:
        return [flow_to_openai_tool(flow) for flow in agentsjson.flows]
    elif format == ToolFormat.JSON:
        return [flow_to_json_tool(flow) for flow in agentsjson.flows]
    else:
        raise ValueError(f"Unsupported tool format: {format}")
    
def flows_tools(flows: List[Flow], format: ToolFormat) -> List[Dict[str, Any]]:
    if format == ToolFormat.OPENAI:
        return [flow_to_openai_tool(flow) for flow in flows]
    elif format == ToolFormat.JSON:
        return [flow_to_json_tool(flow) for flow in flows]
    else:
        raise ValueError(f"Unsupported tool format: {format}")
    
def flows_prompt(flows: List[Flow]) -> str:
    """A slim representation of flows to add to an LLM system prompt"""    
    return "\n".join([f"{flow.id}: {flow.description}" for flow in flows])

def flow_to_openai_tool(flow: Flow) -> Dict[str, Any]:
    """Convert a Flow to an OpenAI function-calling tool format"""
    def convert_schema_to_openai(schema: Dict[str, Any]) -> Dict[str, Any]:
        """Helper function to convert JSON schema to OpenAI format recursively"""
        if "oneOf" in schema:
            # Simply convert oneOf to anyOf while preserving the base schema structure
            converted = schema.copy()
            converted["anyOf"] = converted.pop("oneOf")
            return convert_schema_to_openai(converted)  # Convert any nested schemas
        elif "anyOf" in schema:
            return {
                "anyOf": [convert_schema_to_openai(option) for option in schema["anyOf"]]
            }
        elif schema.get("type") == "object" and "properties" in schema:
            properties = {}
            for prop_name, prop_schema in schema["properties"].items():
                properties[prop_name] = convert_schema_to_openai(prop_schema)
            result = {
                "type": "object",
                "properties": properties
            }
            if "required" in schema:
                result["required"] = schema["required"]
            return result
        elif schema.get("type") == "array" and "items" in schema:
            return {
                "type": "array",
                "items": convert_schema_to_openai(schema["items"])
            }
        else:
            result = {
                "type": schema.get("type", "string"),
                "description": schema.get("description", "")
            }
            if "enum" in schema:
                result["enum"] = schema["enum"]
            if "format" in schema:
                result["format"] = schema["format"]
            return result

    properties = {}
    
    # Handle parameters
    if flow.fields.parameters:
        properties["parameters"] = {
            "type": "object",
            "properties": {
                param.name: {
                    **({"type": param.type, "items": {"type": "string"}} if param.type == "array" else {"type": param.type if hasattr(param, 'type') else "string"}),  # Handle array type with items
                    "description": param.description
                }
                for param in flow.fields.parameters
            },
            "required": [param.name for param in flow.fields.parameters if param.required]
        }

    # Handle request body
    if flow.fields.requestBody and flow.fields.requestBody.content:
        content_type = ("application/json" 
                       if "application/json" in flow.fields.requestBody.content 
                       else next(iter(flow.fields.requestBody.content)))
        
        content = flow.fields.requestBody.content[content_type]        
        if content.schema_:
            converted_request_body = convert_schema_to_openai(content.schema_)
            properties["requestBody"] = converted_request_body

    return {
        "type": "function",
        "function": {
            "name": flow.id,
            "description": flow.description,
            "parameters": {
                "type": "object",
                "properties": properties,
                "required": [key for key in properties.keys()]
            },
            "additionalProperties": False
        }
    }
    
def flow_to_json_tool(flow: Flow) -> str:
    """Convert a Flow to a JSON tool format"""
    return {
        "type": "function",
        "function": {
            "name": flow.id,
            "description": flow.description,
            "parameters": flow.fields
        }
    }
    
    
    

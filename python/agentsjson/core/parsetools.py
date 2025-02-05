from enum import Enum
import logging
from typing import List, Dict, Any
from .models.tools import ToolFormat
from .models.schema import Flow

# Configure logging
logger = logging.getLogger(__name__)

def configure_logging(debug: bool = False):
    """Configure logging level and format"""
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
def flows_tools(flows: List[Flow], format: ToolFormat) -> List[Dict[str, Any]]:
    """Convert flows to tool format for LLM consumption"""
    logger.debug(f"Converting {len(flows)} flows to {format} format")
    
    if format == ToolFormat.OPENAI:
        tools = [flow_to_openai_tool(flow) for flow in flows]
        logger.debug(f"Generated {len(tools)} OpenAI tools")
        return tools
    elif format == ToolFormat.JSON:
        tools = [flow_to_json_tool(flow) for flow in flows]
        logger.debug(f"Generated {len(tools)} JSON tools")
        return tools
    else:
        error_msg = f"Unsupported tool format: {format}"
        logger.error(error_msg)
        raise ValueError(error_msg)
    
def flows_prompt(flows: List[Flow]) -> str:
    """A slim representation of flows to add to an LLM system prompt"""    
    logger.debug(f"Generating prompt for {len(flows)} flows")
    prompt = "\n".join([f"{flow.id}: {flow.description}" for flow in flows])
    logger.debug(f"Generated prompt:\n{prompt}")
    return prompt

def flow_to_openai_tool(flow: Flow) -> Dict[str, Any]:
    """Convert a Flow to an OpenAI function-calling tool format"""
    logger.debug(f"Converting flow '{flow.id}' to OpenAI tool format")
    
    def convert_schema_to_openai(schema: Dict[str, Any]) -> Dict[str, Any]:
        """Helper function to convert JSON schema to OpenAI format recursively"""
        logger.debug(f"Converting schema: {schema}")
        
        if "anyOf" in schema:
            logger.debug("Processing anyOf schema")
            return {
                "anyOf": [convert_schema_to_openai(option) for option in schema["anyOf"]]
            }
        elif schema.get("type") == "object" and "properties" in schema:
            logger.debug("Processing object schema with properties")
            properties = {}
            for prop_name, prop_schema in schema["properties"].items():
                logger.debug(f"Converting property: {prop_name}")
                properties[prop_name] = convert_schema_to_openai(prop_schema)
            result = {
                "type": "object",
                "properties": properties
            }
            if "required" in schema:
                result["required"] = schema["required"]
            return result
        elif schema.get("type") == "array" and "items" in schema:
            logger.debug("Processing array schema")
            return {
                "type": "array",
                "items": convert_schema_to_openai(schema["items"])
            }
        else:
            logger.debug("Processing simple schema")
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
        logger.debug(f"Processing {len(flow.fields.parameters)} parameters")
        properties["parameters"] = {
            "type": "object",
            "properties": {
                param.name: {
                    "type": "string",  # TODO: add type based on param.type if available
                    "description": param.description
                }
                for param in flow.fields.parameters
            },
            "required": [param.name for param in flow.fields.parameters if param.required]
        }

    # Handle request body
    if flow.fields.requestBody and flow.fields.requestBody.content:
        logger.debug("Processing request body")
        content_type = ("application/json" 
                       if "application/json" in flow.fields.requestBody.content 
                       else next(iter(flow.fields.requestBody.content)))
        
        content = flow.fields.requestBody.content[content_type]        
        if content.schema_:
            logger.debug(f"Converting request body schema for content type: {content_type}")
            converted_request_body = convert_schema_to_openai(content.schema_)
            properties["requestBody"] = converted_request_body

    tool = {
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
    
    logger.debug(f"Generated OpenAI tool for flow '{flow.id}'")
    return tool
    
def flow_to_json_tool(flow: Flow) -> str:
    """Convert a Flow to a JSON tool format"""
    logger.debug(f"Converting flow '{flow.id}' to JSON tool format")
    tool = {
        "type": "function",
        "function": {
            "name": flow.id,
            "description": flow.description,
            "parameters": flow.fields
        }
    }
    logger.debug(f"Generated JSON tool for flow '{flow.id}'")
    return tool
    
    
    

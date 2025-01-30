import requests
import yaml
from typing import Dict, Any, List
from benedict import benedict
from pydantic import ValidationError

from .utils import convert_dot_digits_to_brackets
from .models.schema import Flow, AgentsJson, Override, Source
from .models.bundle import Bundle

def apply_overrides(openapi_source: Dict[str, Any], overrides: List[Override]) -> Dict[str, Any]:
    """
    Apply a list of overrides to an OpenAPI source document.
    """
    d = benedict(openapi_source, keypath_separator='!')
    
    for override in overrides:
        if override.fieldPath and override.value is not None:
            field_path = convert_dot_digits_to_brackets(override.fieldPath)
            d[field_path] = override.value
            
    return dict(d)

def load_openapi_source(source: Source) -> Dict[str, Any]:
    """
    Load an OpenAPI source document from a URL. Resolves all refs in the spec.
    """    
    with requests.get(source.path) as response:
        if response.status_code != 200:
            raise Exception(f"Failed to fetch OpenAPI spec from {source.path}: {response.status_code}")
        
        
        # Parse based on file extension
        parsed_data = None
        if source.path.lower().endswith(('.yml', '.yaml')):
            parsed_data = yaml.safe_load(response.text)
        elif source.path.lower().endswith('.json'):
            parsed_data = response.json()
        else:
            raise ValueError(f"Unsupported file extension for OpenAPI spec: {source.path}")
        
        return parsed_data

def index_by_operation_id(spec: Dict[str, Any]) -> Dict[str, Any]:
    """
    Creates a dictionary mapping operationIds to their operation info from an OpenAPI spec.
    """
    http_methods = ('get', 'post', 'put', 'delete', 'patch', 'options', 'head')
    
    return {
        path_item.get(method).get('operationId'): {
            **path_item.get(method),
            'path': path,
            'method': method
        }
        for path, path_item in spec.get('paths', {}).items()
        for method in http_methods
        if path_item.get(method) and path_item.get(method).get('operationId')
    }

def load_agents_json(url: str) -> Bundle:
    """
    Loads an agents.json file and returns a Bundle containing the parsed agents.json, the OpenAPI spec, and the indexed operations.
    """
    with requests.get(url) as response:
        if response.status_code != 200:
            raise Exception(f"Failed to fetch agents.json from {url}: {response.status_code}")
        
        # Try to parse the response content
        content = response.text.strip()
        if not content:
            raise ValueError("Empty response received")
                
        agents_json = AgentsJson.model_validate(response.json())
        
        source: Source = next(source for source in agents_json.sources)
        openapi_source = load_openapi_source(source)
        
        # Modify and index the OpenAPI spec
        openapi_source = apply_overrides(openapi_source, overrides=agents_json.overrides or [])
        indexed_spec = index_by_operation_id(openapi_source)
        
        return Bundle(
            agentsJson=agents_json,
            openapi=openapi_source,
            operations=indexed_spec
        )

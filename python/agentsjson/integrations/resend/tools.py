from agentsjson.core.models.auth import AuthConfig
from . import resend_client
from typing import Any, Dict, Type, Optional
import inspect
import importlib
import re


def get_positional_args(func):
    sig = inspect.signature(func)
    return [p.name for p in sig.parameters.values() 
            if p.default == inspect.Parameter.empty 
            and p.name not in ('self', 'kwargs')]

def construct_model(model_class: Type[Any], **kwargs) -> Any:
    """
    Construct a model instance from raw parameters, handling special cases
    """
    # Handle special parameter mappings (like 'from' -> '_from')
    if hasattr(model_class, 'attribute_map'):
        mapped_kwargs = {}
        reverse_attr_map = {v: k for k, v in model_class.attribute_map.items()}
        for key, value in kwargs.items():
            if key in reverse_attr_map:
                mapped_kwargs[reverse_attr_map[key]] = value
            else:
                mapped_kwargs[key] = value
        kwargs = mapped_kwargs

    # Handle list fields by ensuring they're lists
    if hasattr(model_class, 'swagger_types'):
        for field, type_hint in model_class.swagger_types.items():
            if field in kwargs:
                # Convert single values to list for list fields
                if type_hint.startswith('list[') and not isinstance(kwargs[field], list):
                    kwargs[field] = [kwargs[field]]
                
                # Recursively construct nested models
                if type_hint.startswith('list[') and kwargs[field]:
                    try:
                        nested_type = type_hint[5:-1]  # Extract type from list[Type]
                        module = importlib.import_module('.models', 'resend_client')
                        nested_class = getattr(module, nested_type)
                        kwargs[field] = [
                            construct_model(nested_class, **item) if isinstance(item, dict) else item 
                            for item in kwargs[field]
                        ]
                    except (ImportError, AttributeError):
                        pass

    return model_class(**kwargs)

class Executor:
    @staticmethod
    def create_client(api_key: str, method_name: str, **kwargs) -> Any:
        """
        Creates and returns a Resend API Client instance based on the method name.

        The method name is used to determine which API client to instantiate.
        For example, a method_name like "resend_get_audiences_by_id" will return an 
        instance of AudiencesApi.

        :param api_key: API key for authentication.
        :param method_name: Name of the method being invoked.
        :return: Instance of the appropriate API client.
        """
        # Mapping between keywords and corresponding API client classes.
        api_mapping = {
            'api_keys': resend_client.APIKeysApi,
            'audiences': resend_client.AudiencesApi,
            'broadcasts': resend_client.BroadcastsApi,
            'contacts': resend_client.ContactsApi,
            'domains': resend_client.DomainsApi,
            'emails': resend_client.EmailsApi,
        }
        
        # Lowercase the method name for case-insensitive matching.
        method_name_lower = method_name.lower()
        selected_client_class = None
        for keyword, client_cls in api_mapping.items():
            if keyword in method_name_lower:
                selected_client_class = client_cls
                break

        # If no matching client is found, default to DefaultApi
        if selected_client_class is None:
            selected_client_class = resend_client.DefaultApi

        configuration = resend_client.Configuration()
        configuration.api_key['api_key'] = api_key
        api_client = resend_client.ApiClient(configuration)
        return selected_client_class(api_client)

    @staticmethod
    def create_api_client(api_key: str) -> resend_client.ApiClient:
        """Create an API client with the given API key"""
        configuration = resend_client.Configuration()
        configuration.api_key['api_key'] = api_key
        return resend_client.ApiClient(configuration)

    @staticmethod
    def get_response_model(bundle: Dict[str, Any]) -> Optional[Type[Any]]:
        """Get the response model class based on the bundle info"""
        if 'responses' in bundle.get('fields', {}):
            response_info = bundle['fields']['responses'].get('success', {})
            if isinstance(response_info, dict) and 'type' in response_info:
                try:
                    module = importlib.import_module('.models', 'resend_client')
                    return getattr(module, response_info['type'])
                except (ImportError, AttributeError):
                    pass
        return None

    @staticmethod
    def get_request_model(bundle: Dict[str, Any]) -> Optional[Type[Any]]:
        """Get the request model class based on the bundle info"""
        request_body = bundle.get('fields', {}).get('requestBody', {})
        if request_body and 'content' in request_body:
            content = request_body['content'].get('application/json', {})
            if 'schema' in content and content['schema'].get('type') == 'object':
                try:
                    module = importlib.import_module('.models', 'resend_client')
                    # Most request bodies in OpenAPI are named with 'Body' suffix
                    return getattr(module, f"{bundle['operationId'].split('_')[-1].title()}Body")
                except (ImportError, AttributeError):
                    pass
        return None

    @staticmethod
    def run_method(api_key: str, bundle: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """
        **DEPRECATED GENERIC HANDLER**
        
        This method previously executed calls via model handling.
        Instead, use the generic REST API handler below.
        """
        api_client = Executor.create_api_client(api_key)
        
        # Extract path parameters from kwargs
        path_params = {}
        query_params = []
        for param in bundle.get('fields', {}).get('parameters', []):
            if param['in'] == 'path' and param['name'] in kwargs:
                path_params[param['name']] = kwargs.pop(param['name'])
            elif param['in'] == 'query' and param['name'] in kwargs:
                query_params.append((param['name'], kwargs.pop(param['name'])))

        # Prepare the request body if needed
        body_params = None
        if bundle.get('fields', {}).get('requestBody', {}).get('required', False):
            request_model = Executor.get_request_model(bundle)
            if request_model:
                body_params = construct_model(request_model, **kwargs)

        # Set up headers
        header_params = {}
        header_params['Accept'] = api_client.select_header_accept(['application/json'])
        header_params['Content-Type'] = api_client.select_header_content_type(['application/json'])

        # Get the response type
        response_type = Executor.get_response_model(bundle)

        # Make the API call
        response = api_client.call_api(
            bundle['path'],
            bundle['method'],
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type=response_type,
            auth_settings=['bearerAuth'],
            _return_http_data_only=True,
            _preload_content=True,
            _request_timeout=None,
            collection_formats={},
        )

        if hasattr(response, 'to_dict'):
            return response.to_dict()
        return response


# ------------------------------------------------------------------------------
# New Generic REST API Handler using the ApiClient directly.
# ------------------------------------------------------------------------------
#
# This handler is intended for generic REST calls against the Resend API.
# It supports only application/json. The caller supplies a URL
# (which may include placeholder parameters such as /emails/{email_id}),
# the HTTP method, a dictionary of parameters, and an optional JSON body.
#
# Any keys in the parameters that match a placeholder in the URL (e.g. "email_id")
# will be substituted into the URL. Any extras are sent as query parameters.
#

class RestApiHandler:
    @staticmethod
    def execute(
        auth_config: AuthConfig,
        method: str,
        resource_path: str,
        parameters: Optional[Dict[str, Any]] = None,
        request_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> Any:
        """
        Execute a generic REST API call against the Resend API using the provided AuthConfig.
        
        :param auth_config: Authentication configuration (Bearer or API key supported).
        :param method: HTTP method (e.g. "GET", "POST", "PATCH", etc.).
        :param resource_path: The endpoint path (e.g. "/emails/{email_id}").
                              Any placeholders defined via curly braces will be replaced
                              with values drawn from the `parameters` dict.
        :param parameters: Dictionary of parameters. Keys matching a placeholder in the URL
                           will be used as path parameters; any other parameters are sent as query parameters.
        :param request_body: The JSON payload for POST/PUT/PATCH requests.
        :param headers: Optional headers to include. Defaults to application/json.
        :return: The JSON-decoded response from the API.
        :raises: ValueError if the auth type is not supported
                ApiException with parsed error details if the API returns an error
        """
        # Extract token from the authentication config.
        # Currently, we support Bearer and API key types.
        from agentsjson.core.models.auth import AuthType
        if auth_config.type == AuthType.BEARER:
            token = auth_config.token
        elif auth_config.type == AuthType.API_KEY:
            token = auth_config.key_value
        else:
            raise ValueError(f"Unsupported auth type '{auth_config.type}' for Resend API calls in the generic handler.")
        
        path_params = {}
        query_params = {}
        if parameters:
            # Find placeholders in the resource_path (e.g. {email_id})
            placeholders = re.findall(r'{(\w+)}', resource_path)
            for key, value in parameters.items():
                if key in placeholders:
                    path_params[key] = value
                else:
                    query_params[key] = value

        # Set default headers if not provided.
        if headers is None:
            headers = {}
        headers.setdefault('Accept', 'application/json')
        headers.setdefault('Content-Type', 'application/json')
        
        # Configure the API client with the extracted token.
        from .resend_client.api_client import ApiClient
        from .resend_client.configuration import Configuration
        from .resend_client.rest import ApiException
        import json
        
        configuration = Configuration()
        
        # Override the auth_settings method to provide proper bearer auth configuration
        def auth_settings(self):
            return {
                'bearerAuth': {
                    'type': 'api_key',
                    'in': 'header',
                    'key': 'Authorization',
                    'value': f'Bearer {token}'
                }
            }
        configuration.auth_settings = auth_settings.__get__(configuration)
        
        client = ApiClient(configuration)
        
        try:
            # Execute the API call using the client.
            response = client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=headers,
                body=request_body,
                post_params=[],
                files={},
                response_type=object,  # Returning a JSON-decoded object.
                auth_settings=['bearerAuth'],
                _return_http_data_only=True,
                _preload_content=True,
                _request_timeout=None,
                collection_formats={}
            )
            
            return response
            
        except ApiException as e:
            # Parse the error response body if it exists
            if e.body:
                try:
                    if isinstance(e.body, bytes):
                        error_data = json.loads(e.body.decode('utf-8'))
                    else:
                        error_data = json.loads(e.body)
                    # Raise a new exception with the parsed error details
                    raise ApiException(
                        status=e.status,
                        reason=f"{error_data.get('name', 'Unknown error')}: {error_data.get('message', str(e))}"
                    )
                except json.JSONDecodeError:
                    # If we can't parse the JSON, raise the original error
                    raise e
            else:
                raise e
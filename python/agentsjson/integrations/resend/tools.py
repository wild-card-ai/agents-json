from agentsjson.core.models.auth import AuthConfig
from typing import Any, Dict, Optional
import re
from .resend_client.api_client import ApiClient
from .resend_client.configuration import Configuration
from .resend_client.rest import ApiException
import json
    
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
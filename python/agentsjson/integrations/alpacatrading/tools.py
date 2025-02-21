from agentsjson.core.models.auth import AuthConfig
from typing import Any, Dict, Optional
import re
from ..resend.resend_client.api_client import ApiClient
from ..resend.resend_client.configuration import Configuration
from ..resend.resend_client.rest import ApiException
import json
from enum import Enum, auto

class AlpacaApiType(Enum):
    TRADING = auto()
    MARKET_DATA = auto()

class RestApiHandler:
    # Live URLs
    TRADING_BASE_URL = "https://api.alpaca.markets"
    MARKET_DATA_BASE_URL = "https://data.alpaca.markets"
    
    # Paper trading URLs
    PAPER_TRADING_BASE_URL = "https://paper-api.alpaca.markets"
    
    @staticmethod
    def execute(
        auth_config: AuthConfig,
        method: str,
        resource_path: str,
        parameters: Optional[Dict[str, Any]] = None,
        request_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        api_type: AlpacaApiType = AlpacaApiType.TRADING,
        use_paper: bool = True
    ) -> Any:
        """
        Execute a generic REST API call against the Alpaca API using the provided AuthConfig.
        
        :param auth_config: Authentication configuration (API key and Basic auth supported).
        :param method: HTTP method (e.g. "GET", "POST", "PATCH", etc.).
        :param resource_path: The endpoint path (e.g. "/v2/orders/{order_id}").
                              Any placeholders defined via curly braces will be replaced
                              with values drawn from the `parameters` dict.
        :param parameters: Dictionary of parameters. Keys matching a placeholder in the URL
                           will be used as path parameters; any other parameters are sent as query parameters.
        :param request_body: The JSON payload for POST/PUT/PATCH requests.
        :param headers: Optional headers to include. Defaults to application/json.
        :param api_type: Which Alpaca API to use (TRADING or MARKET_DATA).
        :param use_paper: Whether to use paper trading URLs (only applies to TRADING api_type).
        :return: The JSON-decoded response from the API.
        :raises: ValueError if the auth type is not supported
                ApiException with parsed error details if the API returns an error
        """
        # Extract API key and secret from the authentication config.
        from agentsjson.core.models.auth import AuthType, UserPassCredentials
        print(f"\nAlpaca API Handler - Auth Config Type: {auth_config.type}")
        
        if auth_config.type == AuthType.API_KEY:
            print("Using API_KEY authentication")
            api_key = auth_config.key_id
            api_secret = auth_config.key_value
        elif auth_config.type == AuthType.BASIC:
            print("Using BASIC authentication")
            # For basic auth, extract username/password from credentials
            if isinstance(auth_config.credentials, UserPassCredentials):
                print("Credentials type: UserPassCredentials")
                api_key = auth_config.credentials.username
                api_secret = auth_config.credentials.password
                print(f"Username length: {len(api_key)}, Password length: {len(api_secret)}")
            elif isinstance(auth_config.credentials, str):
                print("Credentials type: string (base64)")
                try:
                    import base64
                    decoded = base64.b64decode(auth_config.credentials).decode('utf-8')
                    api_key, api_secret = decoded.split(':')
                    print("Successfully decoded base64 credentials")
                except Exception as e:
                    print(f"Error decoding base64 credentials: {str(e)}")
                    raise ValueError(f"Invalid basic auth credentials string: {str(e)}")
            else:
                print(f"Invalid credentials type: {type(auth_config.credentials)}")
                raise ValueError("Invalid basic auth credentials format")
        else:
            print(f"Unsupported auth type: {auth_config.type}")
            raise ValueError(f"Unsupported auth type '{auth_config.type}' for Alpaca API calls")
        
        if not api_key or not api_secret:
            print("Missing API key or secret key")
            raise ValueError("Missing API key or secret key")
            
        print(f"API Key length: {len(api_key)}, Secret length: {len(api_secret)}")
        
        path_params = {}
        query_params = {}
        if parameters:
            # Find placeholders in the resource_path (e.g. {order_id})
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
        headers.setdefault('APCA-API-KEY-ID', api_key)
        headers.setdefault('APCA-API-SECRET-KEY', api_secret)
        
        configuration = Configuration()
        
        # Select the appropriate base URL based on API type and paper trading preference
        if api_type == AlpacaApiType.MARKET_DATA:
            configuration.host = RestApiHandler.MARKET_DATA_BASE_URL
        else:  # TRADING
            configuration.host = RestApiHandler.PAPER_TRADING_BASE_URL if use_paper else RestApiHandler.TRADING_BASE_URL
        
        print(f"\nAPI Request Setup:")
        print(f"Base URL: {configuration.host}")
        print(f"Method: {method}")
        print(f"Resource path: {resource_path}")
        print(f"Path params: {path_params}")
        print(f"Query params: {query_params}")
        print(f"Request body: {request_body}")
        print(f"Headers: {list(headers.keys())}")
        
        client = ApiClient(configuration)
        
        try:
            print("\nExecuting API call...")
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
                auth_settings=[],  # We handle auth via headers
                _return_http_data_only=True,
                _preload_content=True,
                _request_timeout=None,
                collection_formats={}
            )
            print("API call successful")
            return response
            
        except ApiException as e:
            print(f"\nAPI call failed:")
            print(f"Status: {e.status}")
            print(f"Reason: {e.reason}")
            print(f"Body: {e.body if isinstance(e.body, str) else e.body.decode('utf-8') if e.body else None}")
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
                        reason=f"{error_data.get('code', 'Unknown error')}: {error_data.get('message', str(e))}"
                    )
                except json.JSONDecodeError:
                    # If we can't parse the JSON, raise the original error
                    raise e
            else:
                raise e

from agentsjson.core.models.auth import AuthConfig
from typing import Any, Dict, Optional
import re
import json
from urllib.parse import urlencode

# Importing all the necessary API clients.
from .theodds_client.api_client import ApiClient
from .theodds_client.configuration import Configuration
from .theodds_client.rest import ApiException
from .theodds_client.api.sports_api import SportsApi
from .theodds_client.api.current_events_api import CurrentEventsApi
from .theodds_client.api.historical_events_api import HistoricalEventsApi
from .theodds_client.api.default_api import DefaultApi

class RestApiHandler:
    @staticmethod
    def get_api_client(operation_id: str, token: str) -> object:
        configuration = Configuration()
        # Set the host explicitly based on the successful curl command.
        configuration.host = "https://api.the-odds-api.com"

        def auth_settings(self):
            # Not used since we inject the key manually but defined for reference.
            return {
                'apiKeyAuth': {
                    'type': 'api_key',
                    'in': 'query',
                    'key': 'apiKey',
                    'value': token
                }
            }
        configuration.auth_settings = auth_settings.__get__(configuration)

        # Mapping based on operation_id.
        if operation_id == "theodds_get_v4_sports":
            return SportsApi(ApiClient(configuration))
        elif operation_id.startswith("theodds_get_v4_sports_events"):
            return CurrentEventsApi(ApiClient(configuration))
        elif operation_id.startswith("theodds_get_v4_sports_odds_by_sport"):
            return CurrentEventsApi(ApiClient(configuration))
        elif operation_id.startswith("theodds_get_v4_sports_scores"):
            return CurrentEventsApi(ApiClient(configuration))
        elif operation_id.startswith("theodds_get_v4_sports_participants"):
            return DefaultApi(ApiClient(configuration))
        elif operation_id.startswith("theodds_get_v4_historical"):
            return HistoricalEventsApi(ApiClient(configuration))
        else:
            # Default fallback
            return DefaultApi(ApiClient(configuration))
    
    @staticmethod
    def execute(
        auth_config: AuthConfig,
        method: str,
        resource_path: str,
        operation_id: str,
        parameters: Optional[Dict[str, Any]] = None,
        request_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> Any:
        from agentsjson.core.models.auth import AuthType
        if auth_config.type == AuthType.BEARER:
            token = auth_config.token
        elif auth_config.type == AuthType.API_KEY:
            token = auth_config.key_value
        else:
            raise ValueError(f"Unsupported auth type '{auth_config.type}'.")

        # Ensure parameters exist.
        if parameters is None:
            parameters = {}

        # Remove an external 'apiKey' param if present to avoid duplication.
        if "apiKey" in parameters:
            parameters.pop("apiKey")
        # Inject the API key under 'api_key' if not already present.
        if auth_config.type == AuthType.API_KEY and "api_key" not in parameters:
            parameters["api_key"] = token

        # Build path and query parameters.
        path_params = {}
        query_params = []
        placeholders = re.findall(r'{(\w+)}', resource_path)

        for key, value in parameters.items():
            if key in placeholders:
                path_params[key] = value
            else:
                # Remap "api_key" to "apiKey".
                query_key = "apiKey" if key == "api_key" else key
                query_params.append((query_key, value))

        if headers is None:
            headers = {}
        headers.setdefault('Accept', 'application/json')
        headers.setdefault('Content-Type', 'application/json')

        client = RestApiHandler.get_api_client(operation_id, token)

        return client.api_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            query_params=query_params,
            header_params=headers,
            body=request_body,
            post_params=[],
            files={},
            response_type=object,  # JSON-decoded response.
            auth_settings=[],  # Using manual key injection.
            _return_http_data_only=True,
            _preload_content=True,
            _request_timeout=None,
            collection_formats={}
        )
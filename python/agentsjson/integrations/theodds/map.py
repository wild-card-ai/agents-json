from typing import Any, Callable, Dict
from .tools import RestApiHandler
from ..types import ExecutorType
map_type = ExecutorType.RESTAPIHANDLER

# Mapping dictionary that defines the HTTP method and resource path for each operation
OPERATION_MAPPING: Dict[str, tuple[str, str]] = {
    "theodds_get_v4_sports": ("GET", "/v4/sports"),
    "theodds_get_v4_sports_odds_by_sport": ("GET", "/v4/sports/{sport}/odds"),
    "theodds_get_v4_sports_scores_by_sport": ("GET", "/v4/sports/{sport}/scores"),
    "theodds_get_v4_sports_events_by_sport": ("GET", "/v4/sports/{sport}/events"),
    "theodds_get_v4_sports_events_odds_by_sport_and_event_id": ("GET", "/v4/sports/{sport}/events/{event_id}/odds"),
    "theodds_get_v4_sports_participants_by_sport": ("GET", "/v4/sports/{sport}/participants"),
    "theodds_get_v4_historical_sports_odds_by_sport": ("GET", "/v4/historical/{sport}/odds"),
    "theodds_get_v4_historical_sports_events_by_sport": ("GET", "/v4/historical/{sport}/events"),
    "theodds_get_v4_historical_sports_events_odds_by_sport_and_event_id": ("GET", "/v4/historical/{sport}/events/{event_id}/odds")
}

def get_lambda(operation_id: str) -> Callable[[str], Dict[str, Any]]:
    """
    Creates a lambda function that executes a REST API call for the given operation.
    
    :param operation_id: The operation ID (e.g. "resend_post_emails")
    :return: A lambda that takes an api_key and kwargs, executing the appropriate REST call
    """
    if operation_id not in OPERATION_MAPPING:
        raise ValueError(f"Operation id {operation_id} not supported")
    
    method, resource_path = OPERATION_MAPPING[operation_id]
    
    # The lambda extracts parameters and request_body from kwargs and passes them to RestApiHandler
    return lambda auth_config, **kwargs: RestApiHandler.execute(
        operation_id=operation_id,
        auth_config=auth_config,
        method=method,
        resource_path=resource_path,
        parameters=kwargs.get("parameters", {}),
        request_body=kwargs.get("requestBody", kwargs.get("request_body", {}))
    )

# Generate the mapping dynamically based on the operation mapping dictionary
map = {op_id: get_lambda(op_id) for op_id in OPERATION_MAPPING}
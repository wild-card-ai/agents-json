from typing import Any, Callable, Dict
from .tools import RestApiHandler
from ..types import ExecutorType
map_type = ExecutorType.RESTAPIHANDLER

# Mapping dictionary that defines the HTTP method and resource path for each operation
OPERATION_MAPPING: Dict[str, tuple[str, str]] = {
    "intercom_get_admins": ("GET", "/admins"),
    "intercom_get_admins_by_admin_id": ("GET", "/admins/{admin_id}"),
    "intercom_get_admins_activity_logs": ("GET", "/admins/activity_logs"),
    "intercom_update_admin_away_mode": ("PATCH", "/admins/away_mode"),
    "intercom_get_admin_availability": ("GET", "/admins/availability"),
    "intercom_update_admin_availability": ("PATCH", "/admins/availability"),
    "intercom_list_contacts": ("GET", "/contacts"),
    "intercom_get_contact_by_id": ("GET", "/contacts/{contact_id}"),
    "intercom_create_contact": ("POST", "/contacts"),
    "intercom_update_contact": ("PATCH", "/contacts/{contact_id}"),
    "intercom_delete_contact": ("DELETE", "/contacts/{contact_id}"),
    "intercom_merge_contact": ("POST", "/contacts/merge"),
    "intercom_restore_contact": ("POST", "/contacts/{contact_id}/restore"),
    "intercom_bulk_contact_create": ("POST", "/contacts/bulk_create"),
    "intercom_bulk_contact_update": ("PATCH", "/contacts/bulk_update"),
    "intercom_search_contacts": ("POST", "/contacts/search"),
    "intercom_list_companies": ("GET", "/companies"),
    "intercom_get_company_by_id": ("GET", "/companies/{company_id}"),
    "intercom_create_company": ("POST", "/companies"),
    "intercom_update_company": ("PATCH", "/companies/{company_id}"),
    "intercom_delete_company": ("DELETE", "/companies/{company_id}"),
    "intercom_merge_company": ("POST", "/companies/merge"),
    "intercom_search_companies": ("POST", "/companies/search"),
    "intercom_list_conversations": ("GET", "/conversations"),
    "intercom_get_conversation_by_id": ("GET", "/conversations/{conversation_id}"),
    "intercom_reply_conversation": ("POST", "/conversations/{conversation_id}/reply"),
    "intercom_archive_conversation": ("POST", "/conversations/{conversation_id}/archive"),
    "intercom_unarchive_conversation": ("POST", "/conversations/{conversation_id}/unarchive"),
    "intercom_mark_conversation_as_read": ("POST", "/conversations/{conversation_id}/mark_read"),
    "intercom_mark_conversation_as_unread": ("POST", "/conversations/{conversation_id}/mark_unread"),
    "intercom_search_conversations": ("POST", "/conversations/search"),
    "intercom_get_conversation_metrics": ("GET", "/conversations/{conversation_id}/metrics"),
    "intercom_list_users": ("GET", "/users"),
    "intercom_get_user_by_id": ("GET", "/users/{user_id}"),
    "intercom_create_user": ("POST", "/users"),
    "intercom_update_user": ("PATCH", "/users/{user_id}"),
    "intercom_delete_user": ("DELETE", "/users/{user_id}"),
    "intercom_merge_user": ("POST", "/users/merge"),
    "intercom_search_users": ("POST", "/users/search"),
    "intercom_list_visitors": ("GET", "/visitors"),
    "intercom_get_visitor_by_id": ("GET", "/visitors/{visitor_id}"),
    "intercom_post_visitors_convert": ("POST", "/visitors/convert"),
    "intercom_create_message": ("POST", "/messages"),
    "intercom_list_messages": ("GET", "/messages"),
    "intercom_get_message_by_id": ("GET", "/messages/{message_id}"),
    "intercom_get_message_metrics": ("GET", "/messages/{message_id}/metrics"),
    "intercom_create_event": ("POST", "/events"),
    "intercom_list_events": ("GET", "/events"),
    "intercom_list_segments": ("GET", "/segments"),
    "intercom_get_segment_by_id": ("GET", "/segments/{segment_id}"),
    "intercom_create_segment": ("POST", "/segments"),
    "intercom_update_segment": ("PATCH", "/segments/{segment_id}"),
    "intercom_delete_segment": ("DELETE", "/segments/{segment_id}"),
    "intercom_list_tags": ("GET", "/tags"),
    "intercom_create_tag": ("POST", "/tags"),
    "intercom_update_tag": ("PATCH", "/tags/{tag_id}"),
    "intercom_delete_tag": ("DELETE", "/tags/{tag_id}"),
    "intercom_add_tag_to_contact": ("POST", "/contacts/{contact_id}/tags"),
    "intercom_remove_tag_from_contact": ("DELETE", "/contacts/{contact_id}/tags/{tag_id}"),
    "intercom_add_tag_to_company": ("POST", "/companies/{company_id}/tags"),
    "intercom_remove_tag_from_company": ("DELETE", "/companies/{company_id}/tags/{tag_id}"),
    "intercom_list_notes": ("GET", "/notes"),
    "intercom_get_note_by_id": ("GET", "/notes/{note_id}"),
    "intercom_create_note": ("POST", "/notes"),
    "intercom_update_note": ("PATCH", "/notes/{note_id}"),
    "intercom_delete_note": ("DELETE", "/notes/{note_id}"),
    "intercom_list_subscription_types": ("GET", "/subscription_types"),
    "intercom_update_subscription": ("PATCH", "/subscriptions/{subscription_id}"),
    "intercom_delete_subscription": ("DELETE", "/subscriptions/{subscription_id}"),
    "intercom_get_settings": ("GET", "/settings"),
    "intercom_update_settings": ("PATCH", "/settings"),
    "intercom_list_webhooks": ("GET", "/webhooks"),
    "intercom_get_webhook_by_id": ("GET", "/webhooks/{webhook_id}"),
    "intercom_create_webhook": ("POST", "/webhooks"),
    "intercom_update_webhook": ("PATCH", "/webhooks/{webhook_id}"),
    "intercom_delete_webhook": ("DELETE", "/webhooks/{webhook_id}"),
    "intercom_create_broadcast": ("POST", "/broadcasts"),
    "intercom_list_broadcasts": ("GET", "/broadcasts"),
    "intercom_get_broadcast_by_id": ("GET", "/broadcasts/{broadcast_id}"),
    "intercom_update_broadcast": ("PATCH", "/broadcasts/{broadcast_id}"),
    "intercom_delete_broadcast": ("DELETE", "/broadcasts/{broadcast_id}"),
    "intercom_get_usage_stats": ("GET", "/usage_stats"),
    "intercom_get_impressions": ("GET", "/impressions"),
    "intercom_list_custom_attributes": ("GET", "/custom_attributes"),
    "intercom_list_inboxes": ("GET", "/inboxes"),
    "intercom_get_reply_metrics": ("GET", "/reply_metrics"),
    "intercom_list_teams": ("GET", "/teams"),
    "intercom_get_team_by_id": ("GET", "/teams/{team_id}"),
    "intercom_create_team": ("POST", "/teams"),
    "intercom_update_team": ("PATCH", "/teams/{team_id}"),
    "intercom_delete_team": ("DELETE", "/teams/{team_id}"),
    "intercom_list_integrations": ("GET", "/integrations"),
    "intercom_get_integration_by_id": ("GET", "/integrations/{integration_id}"),
    "intercom_create_integration": ("POST", "/integrations"),
    "intercom_update_integration": ("PATCH", "/integrations/{integration_id}"),
    "intercom_delete_integration": ("DELETE", "/integrations/{integration_id}"),
    "intercom_close_conversation": ("POST", "/conversations/{conversation_id}/close"),
    "intercom_open_conversation": ("POST", "/conversations/{conversation_id}/open"),
    "intercom_reassign_conversation": ("POST", "/conversations/{conversation_id}/reassign"),
    "intercom_get_conversation_summary": ("GET", "/conversations/{conversation_id}/summary"),
    "intercom_get_conversation_stats": ("GET", "/conversations/{conversation_id}/stats"),
    "intercom_subscribe_contact": ("POST", "/contacts/{contact_id}/subscribe"),
    "intercom_unsubscribe_contact": ("POST", "/contacts/{contact_id}/unsubscribe"),
    "intercom_list_leads": ("GET", "/leads"),
    "intercom_get_lead_by_id": ("GET", "/leads/{lead_id}"),
    "intercom_convert_lead_to_user": ("POST", "/leads/convert"),
    "intercom_update_lead": ("PATCH", "/leads/{lead_id}"),
    "intercom_delete_lead": ("DELETE", "/leads/{lead_id}")
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
        auth_config=auth_config,
        method=method,
        resource_path=resource_path,
        parameters=kwargs.get("parameters", {}),
        request_body=kwargs.get("requestBody", kwargs.get("request_body", {}))
    )

# Generate the mapping dynamically based on the operation mapping dictionary
map = {op_id: get_lambda(op_id) for op_id in OPERATION_MAPPING}
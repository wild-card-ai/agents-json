from typing import Any, Callable, Dict
from .tools import RestApiHandler
from ..types import ExecutorType
map_type = ExecutorType.RESTAPIHANDLER

OPERATION_MAPPING = {
    # Alert Events
    "rootly_list_alert_events": ("GET", "/v1/alert_events"),
    "rootly_get_alert_event": ("GET", "/v1/alert_events/{id}"),
    
    # Alert Groups
    "rootly_create_alert_group": ("POST", "/v1/alert_groups"),
    "rootly_list_alert_groups": ("GET", "/v1/alert_groups"),
    "rootly_get_alert_group": ("GET", "/v1/alert_groups/{id}"),
    "rootly_update_alert_group": ("PATCH", "/v1/alert_groups/{id}"),
    "rootly_delete_alert_group": ("DELETE", "/v1/alert_groups/{id}"),
    
    # Alert Urgencies
    "rootly_create_alert_urgency": ("POST", "/v1/alert_urgencies"),
    "rootly_list_alert_urgencies": ("GET", "/v1/alert_urgencies"),
    "rootly_get_alert_urgency": ("GET", "/v1/alert_urgencies/{id}"),
    "rootly_update_alert_urgency": ("PATCH", "/v1/alert_urgencies/{id}"),
    "rootly_delete_alert_urgency": ("DELETE", "/v1/alert_urgencies/{id}"),
    
    # Alert Sources
    "rootly_create_alerts_source": ("POST", "/v1/alerts_sources"),
    "rootly_list_alerts_sources": ("GET", "/v1/alerts_sources"),
    "rootly_get_alerts_source": ("GET", "/v1/alerts_sources/{id}"),
    "rootly_update_alerts_source": ("PATCH", "/v1/alerts_sources/{id}"),
    "rootly_delete_alerts_source": ("DELETE", "/v1/alerts_sources/{id}"),
    
    # Alerts
    "rootly_attach_alert": ("POST", "/v1/incidents/{incident_id}/alerts"),
    "rootly_list_incident_alerts": ("GET", "/v1/incidents/{incident_id}/alerts"),
    "rootly_create_alert": ("POST", "/v1/alerts"),
    "rootly_list_alerts": ("GET", "/v1/alerts"),
    "rootly_get_alert": ("GET", "/v1/alerts/{id}"),
    "rootly_acknowledge_alert": ("POST", "/v1/alerts/{id}/acknowledge"),
    "rootly_resolve_alert": ("POST", "/v1/alerts/{id}/resolve"),
    
    # Audits
    "rootly_list_audits": ("GET", "/v1/audits"),
    
    # Authorizations
    "rootly_create_authorization": ("POST", "/v1/authorizations"),
    "rootly_list_authorizations": ("GET", "/v1/authorizations"),
    "rootly_get_authorization": ("GET", "/v1/authorizations/{id}"),
    "rootly_update_authorization": ("PATCH", "/v1/authorizations/{id}"),
    "rootly_delete_authorization": ("DELETE", "/v1/authorizations/{id}"),
    
    # Catalog Entities
    "rootly_create_catalog_entity": ("POST", "/v1/catalog_entities"),
    "rootly_list_catalog_entities": ("GET", "/v1/catalog_entities"),
    "rootly_get_catalog_entity": ("GET", "/v1/catalog_entities/{id}"),
    "rootly_update_catalog_entity": ("PATCH", "/v1/catalog_entities/{id}"),
    "rootly_delete_catalog_entity": ("DELETE", "/v1/catalog_entities/{id}"),
    
    # Catalog Entity Properties
    "rootly_create_catalog_entity_property": ("POST", "/v1/catalog_entity_properties"),
    "rootly_list_catalog_entity_properties": ("GET", "/v1/catalog_entity_properties"),
    "rootly_get_catalog_entity_property": ("GET", "/v1/catalog_entity_properties/{id}"),
    "rootly_update_catalog_entity_property": ("PATCH", "/v1/catalog_entity_properties/{id}"),
    "rootly_delete_catalog_entity_property": ("DELETE", "/v1/catalog_entity_properties/{id}"),
    
    # Catalog Fields
    "rootly_create_catalog_field": ("POST", "/v1/catalog_fields"),
    "rootly_list_catalog_fields": ("GET", "/v1/catalog_fields"),
    "rootly_get_catalog_field": ("GET", "/v1/catalog_fields/{id}"),
    "rootly_update_catalog_field": ("PATCH", "/v1/catalog_fields/{id}"),
    "rootly_delete_catalog_field": ("DELETE", "/v1/catalog_fields/{id}"),
    
    # Catalogs
    "rootly_create_catalog": ("POST", "/v1/catalogs"),
    "rootly_list_catalogs": ("GET", "/v1/catalogs"),
    "rootly_get_catalog": ("GET", "/v1/catalogs/{id}"),
    "rootly_update_catalog": ("PATCH", "/v1/catalogs/{id}"),
    "rootly_delete_catalog": ("DELETE", "/v1/catalogs/{id}"),
    
    # Causes
    "rootly_create_cause": ("POST", "/v1/causes"),
    "rootly_list_causes": ("GET", "/v1/causes"),
    "rootly_get_cause": ("GET", "/v1/causes/{id}"),
    "rootly_update_cause": ("PATCH", "/v1/causes/{id}"),
    "rootly_delete_cause": ("DELETE", "/v1/causes/{id}"),
    
    # Custom Fields
    "rootly_create_custom_field": ("POST", "/v1/custom_fields"),
    "rootly_list_custom_fields": ("GET", "/v1/custom_fields"),
    "rootly_get_custom_field": ("GET", "/v1/custom_fields/{id}"),
    "rootly_update_custom_field": ("PATCH", "/v1/custom_fields/{id}"),
    "rootly_delete_custom_field": ("DELETE", "/v1/custom_fields/{id}"),
    
    # Custom Field Options
    "rootly_create_custom_field_option": ("POST", "/v1/custom_field_options"),
    "rootly_list_custom_field_options": ("GET", "/v1/custom_field_options"),
    "rootly_get_custom_field_option": ("GET", "/v1/custom_field_options/{id}"),
    "rootly_update_custom_field_option": ("PATCH", "/v1/custom_field_options/{id}"),
    "rootly_delete_custom_field_option": ("DELETE", "/v1/custom_field_options/{id}"),
    
    # Custom Forms
    "rootly_create_custom_form": ("POST", "/v1/custom_forms"),
    "rootly_list_custom_forms": ("GET", "/v1/custom_forms"),
    "rootly_get_custom_form": ("GET", "/v1/custom_forms/{id}"),
    "rootly_update_custom_form": ("PATCH", "/v1/custom_forms/{id}"),
    "rootly_delete_custom_form": ("DELETE", "/v1/custom_forms/{id}"),
    
    # Dashboard Panels
    "rootly_create_dashboard_panel": ("POST", "/v1/dashboard_panels"),
    "rootly_list_dashboard_panels": ("GET", "/v1/dashboard_panels"),
    "rootly_duplicate_dashboard_panel": ("POST", "/v1/dashboard_panels/{id}/duplicate"),
    "rootly_get_dashboard_panel": ("GET", "/v1/dashboard_panels/{id}"),
    "rootly_update_dashboard_panel": ("PATCH", "/v1/dashboard_panels/{id}"),
    "rootly_delete_dashboard_panel": ("DELETE", "/v1/dashboard_panels/{id}"),
    
    # Dashboards
    "rootly_create_dashboard": ("POST", "/v1/dashboards"),
    "rootly_list_dashboards": ("GET", "/v1/dashboards"),
    "rootly_duplicate_dashboard": ("POST", "/v1/dashboards/{id}/duplicate"),
    "rootly_set_default_dashboard": ("POST", "/v1/dashboards/{id}/set_default"),
    "rootly_get_dashboard": ("GET", "/v1/dashboards/{id}"),
    "rootly_update_dashboard": ("PATCH", "/v1/dashboards/{id}"),
    "rootly_delete_dashboard": ("DELETE", "/v1/dashboards/{id}"),
    
    # Environments
    "rootly_create_environment": ("POST", "/v1/environments"),
    "rootly_list_environments": ("GET", "/v1/environments"),
    "rootly_get_environment": ("GET", "/v1/environments/{id}"),
    "rootly_update_environment": ("PATCH", "/v1/environments/{id}"),
    "rootly_delete_environment": ("DELETE", "/v1/environments/{id}"),
    
    # Escalation Policies
    "rootly_create_escalation_policy": ("POST", "/v1/escalation_policies"),
    "rootly_list_escalation_policies": ("GET", "/v1/escalation_policies"),
    "rootly_get_escalation_policy": ("GET", "/v1/escalation_policies/{id}"),
    "rootly_update_escalation_policy": ("PATCH", "/v1/escalation_policies/{id}"),
    "rootly_delete_escalation_policy": ("DELETE", "/v1/escalation_policies/{id}"),
    
    # Escalation Levels
    "rootly_create_escalation_level": ("POST", "/v1/escalation_levels"),
    "rootly_list_escalation_levels": ("GET", "/v1/escalation_levels"),
    "rootly_create_escalation_level_paths": ("POST", "/v1/escalation_levels_paths"),
    "rootly_list_escalation_levels_paths": ("GET", "/v1/escalation_levels_paths"),
    "rootly_get_escalation_level": ("GET", "/v1/escalation_levels/{id}"),
    "rootly_update_escalation_level": ("PATCH", "/v1/escalation_levels/{id}"),
    "rootly_delete_escalation_level": ("DELETE", "/v1/escalation_levels/{id}"),
    
    # Functionalities
    "rootly_create_functionality": ("POST", "/v1/functionalities"),
    "rootly_list_functionalities": ("GET", "/v1/functionalities"),
    "rootly_get_functionality": ("GET", "/v1/functionalities/{id}"),
    "rootly_update_functionality": ("PATCH", "/v1/functionalities/{id}"),
    "rootly_delete_functionality": ("DELETE", "/v1/functionalities/{id}"),
    
    # Incidents
    "rootly_create_incident": ("POST", "/v1/incidents"),
    "rootly_list_incidents": ("GET", "/v1/incidents"),
    "rootly_get_incident": ("GET", "/v1/incidents/{id}"),
    "rootly_update_incident": ("PATCH", "/v1/incidents/{id}"),
    "rootly_delete_incident": ("DELETE", "/v1/incidents/{id}"),
    "rootly_acknowledge_incident": ("POST", "/v1/incidents/{id}/acknowledge"),
    "rootly_resolve_incident": ("POST", "/v1/incidents/{id}/resolve"),
    "rootly_start_incident": ("POST", "/v1/incidents/{id}/start"),
    "rootly_assign_incident": ("POST", "/v1/incidents/{id}/assign"),
    "rootly_unassign_incident": ("POST", "/v1/incidents/{id}/unassign"),
    "rootly_add_incident_responder": ("POST", "/v1/incidents/{id}/add_responder"),
    "rootly_remove_incident_responder": ("POST", "/v1/incidents/{id}/remove_responder"),
    
    # Incident Roles
    "rootly_create_incident_role": ("POST", "/v1/incident_roles"),
    "rootly_list_incident_roles": ("GET", "/v1/incident_roles"),
    "rootly_get_incident_role": ("GET", "/v1/incident_roles/{id}"),
    "rootly_update_incident_role": ("PATCH", "/v1/incident_roles/{id}"),
    "rootly_delete_incident_role": ("DELETE", "/v1/incident_roles/{id}"),
    
    # Incident Types
    "rootly_create_incident_type": ("POST", "/v1/incident_types"),
    "rootly_list_incident_types": ("GET", "/v1/incident_types"),
    "rootly_get_incident_type": ("GET", "/v1/incident_types/{id}"),
    "rootly_update_incident_type": ("PATCH", "/v1/incident_types/{id}"),
    "rootly_delete_incident_type": ("DELETE", "/v1/incident_types/{id}"),
    
    # Severities
    "rootly_create_severity": ("POST", "/v1/severities"),
    "rootly_list_severities": ("GET", "/v1/severities"),
    "rootly_get_severity": ("GET", "/v1/severities/{id}"),
    "rootly_update_severity": ("PATCH", "/v1/severities/{id}"),
    "rootly_delete_severity": ("DELETE", "/v1/severities/{id}"),
    
    # Services
    "rootly_create_service": ("POST", "/v1/services"),
    "rootly_list_services": ("GET", "/v1/services"),
    "rootly_get_service": ("GET", "/v1/services/{id}"),
    "rootly_update_service": ("PATCH", "/v1/services/{id}"),
    "rootly_delete_service": ("DELETE", "/v1/services/{id}"),
    
    # Tasks
    "rootly_create_task": ("POST", "/v1/tasks"),
    "rootly_list_tasks": ("GET", "/v1/tasks"),
    "rootly_get_task": ("GET", "/v1/tasks/{id}"),
    "rootly_update_task": ("PATCH", "/v1/tasks/{id}"),
    "rootly_delete_task": ("DELETE", "/v1/tasks/{id}"),
    
    # Teams
    "rootly_create_team": ("POST", "/v1/teams"),
    "rootly_list_teams": ("GET", "/v1/teams"),
    "rootly_get_team": ("GET", "/v1/teams/{id}"),
    "rootly_update_team": ("PATCH", "/v1/teams/{id}"),
    "rootly_delete_team": ("DELETE", "/v1/teams/{id}"),
    
    # Users
    "rootly_list_users": ("GET", "/v1/users"),
    "rootly_get_user": ("GET", "/v1/users/{id}"),
    "rootly_update_user": ("PATCH", "/v1/users/{id}"),
    "rootly_delete_user": ("DELETE", "/v1/users/{id}"),
    
    # Workflows
    "rootly_create_workflow": ("POST", "/v1/workflows"),
    "rootly_list_workflows": ("GET", "/v1/workflows"),
    "rootly_get_workflow": ("GET", "/v1/workflows/{id}"),
    "rootly_update_workflow": ("PATCH", "/v1/workflows/{id}"),
    "rootly_delete_workflow": ("DELETE", "/v1/workflows/{id}"),
    "rootly_trigger_workflow": ("POST", "/v1/workflows/{id}/trigger")
}

def get_lambda(operation_id: str) -> Callable[[str], Dict[str, Any]]:
    """
    Creates a lambda function that executes a REST API call for the given operation.
    
    :param operation_id: The operation ID (e.g. "rootly_list_alert_events")
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
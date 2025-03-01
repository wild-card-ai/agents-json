from .tools import Executor
from ..types import ExecutorType

# Define the type of execution (SDK in this case, since we're using the Google Calendar API client)
map_type = ExecutorType.SDK

# Mapping of operation IDs to corresponding function implementations
map = {
    # Calendar Operations
    "google_calendar_calendars_insert": Executor.google_calendar_calendars_insert,
    "google_calendar_calendars_delete": Executor.google_calendar_calendars_delete,
    "google_calendar_calendars_get": Executor.google_calendar_calendars_get,
    "google_calendar_calendars_patch": Executor.google_calendar_calendars_patch,
    "google_calendar_calendars_update": Executor.google_calendar_calendars_update,
    "google_calendar_calendars_clear": Executor.google_calendar_calendars_clear,

    # Event Operations
    "google_calendar_events_list": Executor.google_calendar_events_list,
    "google_calendar_events_insert": Executor.google_calendar_events_insert,
    "google_calendar_events_import": Executor.google_calendar_events_import,
    "google_calendar_events_quick_add": Executor.google_calendar_events_quick_add,
    "google_calendar_events_watch": Executor.google_calendar_events_watch,
    "google_calendar_events_delete": Executor.google_calendar_events_delete,
    "google_calendar_events_get": Executor.google_calendar_events_get,
    "google_calendar_events_patch": Executor.google_calendar_events_patch,
    "google_calendar_events_update": Executor.google_calendar_events_update,
    "google_calendar_events_instances": Executor.google_calendar_events_instances,
    "google_calendar_events_move": Executor.google_calendar_events_move,

    # ACL Operations
    "google_calendar_acl_list": Executor.google_calendar_acl_list,
    "google_calendar_acl_insert": Executor.google_calendar_acl_insert,
    "google_calendar_acl_watch": Executor.google_calendar_acl_watch,
    "google_calendar_acl_delete": Executor.google_calendar_acl_delete,
    "google_calendar_acl_get": Executor.google_calendar_acl_get,
    "google_calendar_acl_patch": Executor.google_calendar_acl_patch,
    "google_calendar_acl_update": Executor.google_calendar_acl_update,

    # Calendar List Operations
    "google_calendar_calendar_list_list": Executor.google_calendar_calendar_list_list,
    "google_calendar_calendar_list_insert": Executor.google_calendar_calendar_list_insert,
    "google_calendar_calendar_list_watch": Executor.google_calendar_calendar_list_watch,
    "google_calendar_calendar_list_delete": Executor.google_calendar_calendar_list_delete,
    "google_calendar_calendar_list_get": Executor.google_calendar_calendar_list_get,
    "google_calendar_calendar_list_patch": Executor.google_calendar_calendar_list_patch,
    "google_calendar_calendar_list_update": Executor.google_calendar_calendar_list_update,

    # Settings Operations
    "google_calendar_settings_list": Executor.google_calendar_settings_list,
    "google_calendar_settings_watch": Executor.google_calendar_settings_watch,
    "google_calendar_settings_get": Executor.google_calendar_settings_get,

    # Other Operations
    "google_calendar_channels_stop": Executor.google_calendar_channels_stop,
    "google_calendar_colors_get": Executor.google_calendar_colors_get,
    "google_calendar_freebusy_query": Executor.google_calendar_freebusy_query,
}
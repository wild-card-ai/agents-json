from pydantic import BaseModel
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build, Resource
from agentsjson.core.models.auth import OAuth2AuthConfig
from typing import Any, Dict
from functools import lru_cache
from googleapiclient.errors import HttpError

class Executor(BaseModel):
    """
    Executor class for Google Calendar API operations.
    
    Uses OAuth2AuthConfig for authentication.
    """

    @staticmethod
    @lru_cache(maxsize=100)
    def _build_service(token: str, refresh_token: str | None, scopes_str: str) -> Resource:
        """
        Creates a Google Calendar service using OAuth2 credentials.
        """
        try:
            credentials = Credentials(
                token=token,
                refresh_token=refresh_token,
                token_uri="https://oauth2.googleapis.com/token",
                scopes=scopes_str.split(",") if scopes_str else ["https://www.googleapis.com/auth/calendar"]
            )
            return build('calendar', 'v3', credentials=credentials)
        except Exception as e:
            raise Exception(f"Failed to build Google Calendar service: {str(e)}")

    @staticmethod
    def _get_calendar_service(auth_config: OAuth2AuthConfig) -> Resource:
        """
        Retrieves a cached Google Calendar service using OAuth2 credentials.
        """
        scopes_str = ",".join(sorted(list(auth_config.scopes))) if auth_config.scopes else ""
        return Executor._build_service(auth_config.token, auth_config.refresh_token, scopes_str)

    @staticmethod
    def google_calendar_calendars_insert(auth_config: OAuth2AuthConfig, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.calendars().insert(body=kwargs).execute()

    @staticmethod
    def google_calendar_calendars_delete(auth_config: OAuth2AuthConfig, calendarId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.calendars().delete(calendarId=calendarId).execute()

    @staticmethod
    def google_calendar_calendars_get(auth_config: OAuth2AuthConfig, calendarId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.calendars().get(calendarId=calendarId, **kwargs).execute()

    @staticmethod
    def google_calendar_calendars_patch(auth_config: OAuth2AuthConfig, calendarId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.calendars().patch(calendarId=calendarId, body=kwargs).execute()

    @staticmethod
    def google_calendar_calendars_update(auth_config: OAuth2AuthConfig, calendarId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.calendars().update(calendarId=calendarId, body=kwargs).execute()

    @staticmethod
    def google_calendar_calendars_clear(auth_config: OAuth2AuthConfig, calendarId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.calendars().clear(calendarId=calendarId).execute()

    @staticmethod
    def google_calendar_events_insert(auth_config: OAuth2AuthConfig, calendarId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.events().insert(calendarId=calendarId, body=kwargs).execute()

    @staticmethod
    def google_calendar_events_delete(auth_config: OAuth2AuthConfig, calendarId: str, eventId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.events().delete(calendarId=calendarId, eventId=eventId, **kwargs).execute()

    @staticmethod
    def google_calendar_events_get(auth_config: OAuth2AuthConfig, calendarId: str, eventId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.events().get(calendarId=calendarId, eventId=eventId, **kwargs).execute()

    @staticmethod
    def google_calendar_events_list(auth_config: OAuth2AuthConfig, calendarId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.events().list(calendarId=calendarId, **kwargs).execute()

    @staticmethod
    def google_calendar_events_patch(auth_config: OAuth2AuthConfig, calendarId: str, eventId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.events().patch(calendarId=calendarId, eventId=eventId, body=kwargs).execute()

    @staticmethod
    def google_calendar_events_update(auth_config: OAuth2AuthConfig, calendarId: str, eventId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.events().update(calendarId=calendarId, eventId=eventId, body=kwargs).execute()

    @staticmethod
    def google_calendar_events_instances(auth_config: OAuth2AuthConfig, calendarId: str, eventId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.events().instances(calendarId=calendarId, eventId=eventId, **kwargs).execute()

    @staticmethod
    def google_calendar_events_move(auth_config: OAuth2AuthConfig, calendarId: str, eventId: str, destination: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.events().move(calendarId=calendarId, eventId=eventId, destination=destination, **kwargs).execute()

    @staticmethod
    def google_calendar_events_quick_add(auth_config: OAuth2AuthConfig, calendarId: str, text: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.events().quickAdd(calendarId=calendarId, text=text, **kwargs).execute()

    @staticmethod
    def google_calendar_events_watch(auth_config: OAuth2AuthConfig, calendarId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.events().watch(calendarId=calendarId, body=kwargs).execute()

    @staticmethod
    def google_calendar_events_import(auth_config: OAuth2AuthConfig, calendarId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.events().import_(calendarId=calendarId, body=kwargs).execute()

    @staticmethod
    def google_calendar_acl_delete(auth_config: OAuth2AuthConfig, calendarId: str, ruleId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.acl().delete(calendarId=calendarId, ruleId=ruleId).execute()

    @staticmethod
    def google_calendar_acl_get(auth_config: OAuth2AuthConfig, calendarId: str, ruleId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.acl().get(calendarId=calendarId, ruleId=ruleId).execute()

    @staticmethod
    def google_calendar_acl_insert(auth_config: OAuth2AuthConfig, calendarId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.acl().insert(calendarId=calendarId, body=kwargs).execute()

    @staticmethod
    def google_calendar_acl_list(auth_config: OAuth2AuthConfig, calendarId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.acl().list(calendarId=calendarId, **kwargs).execute()

    @staticmethod
    def google_calendar_acl_update(auth_config: OAuth2AuthConfig, calendarId: str, ruleId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.acl().update(calendarId=calendarId, ruleId=ruleId, body=kwargs).execute()

    @staticmethod
    def google_calendar_acl_watch(auth_config: OAuth2AuthConfig, calendarId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.acl().watch(calendarId=calendarId, body=kwargs).execute()

    @staticmethod
    def google_calendar_acl_patch(auth_config: OAuth2AuthConfig, calendarId: str, ruleId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.acl().patch(calendarId=calendarId, ruleId=ruleId, body=kwargs).execute()

    @staticmethod
    def google_calendar_calendar_list_list(auth_config: OAuth2AuthConfig, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.calendarList().list(**kwargs).execute()

    @staticmethod
    def google_calendar_calendar_list_insert(auth_config: OAuth2AuthConfig, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.calendarList().insert(body=kwargs).execute()

    @staticmethod
    def google_calendar_calendar_list_watch(auth_config: OAuth2AuthConfig, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.calendarList().watch(body=kwargs).execute()

    @staticmethod
    def google_calendar_calendar_list_delete(auth_config: OAuth2AuthConfig, calendarId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.calendarList().delete(calendarId=calendarId).execute()

    @staticmethod
    def google_calendar_calendar_list_get(auth_config: OAuth2AuthConfig, calendarId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.calendarList().get(calendarId=calendarId).execute()

    @staticmethod
    def google_calendar_calendar_list_patch(auth_config: OAuth2AuthConfig, calendarId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.calendarList().patch(calendarId=calendarId, body=kwargs).execute()

    @staticmethod
    def google_calendar_calendar_list_update(auth_config: OAuth2AuthConfig, calendarId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.calendarList().update(calendarId=calendarId, body=kwargs).execute()

    @staticmethod
    def google_calendar_settings_list(auth_config: OAuth2AuthConfig, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.settings().list(**kwargs).execute()

    @staticmethod
    def google_calendar_settings_watch(auth_config: OAuth2AuthConfig, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.settings().watch(body=kwargs).execute()

    @staticmethod
    def google_calendar_settings_get(auth_config: OAuth2AuthConfig, setting: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.settings().get(setting=setting).execute()

    @staticmethod
    def google_calendar_colors_get(auth_config: OAuth2AuthConfig, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.colors().get().execute()

    @staticmethod
    def google_calendar_channels_stop(auth_config: OAuth2AuthConfig, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.channels().stop(body=kwargs).execute()

    @staticmethod
    def google_calendar_freebusy_query(auth_config: OAuth2AuthConfig, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.freebusy().query(body=kwargs).execute()

    @staticmethod
    def auto_generate_agenda(auth_config: OAuth2AuthConfig, calendarId: str, eventId: str, **kwargs):
        return {"status": "success", "agenda": "1. Project updates\n2. Next steps\n3. Q&A"}

    @staticmethod
    def smart_event_categorization(auth_config: OAuth2AuthConfig, calendarId: str, eventId: str, **kwargs):
        return {"status": "success", "category": "Work Meeting"}

    @staticmethod
    def predict_best_meeting_time(auth_config: OAuth2AuthConfig, calendarId: str, attendeeEmails: list, **kwargs):
        return {"status": "success", "best_times": ["Monday 10 AM", "Wednesday 3 PM"]}

    @staticmethod
    def bulk_delete_events(auth_config: OAuth2AuthConfig, calendarId: str, eventIds: list, **kwargs):
        results = []
        for eventId in eventIds:
            result = Executor.google_calendar_events_delete(auth_config, calendarId, eventId)
            results.append(result)
        return {"status": "success", "deleted_events": results}

    @staticmethod
    def bulk_update_events(auth_config: OAuth2AuthConfig, calendarId: str, updates: list, **kwargs):
        results = []
        for update in updates:
            eventId = update.get("eventId")
            result = Executor.google_calendar_events_update(auth_config, calendarId, eventId, **update)
            results.append(result)
        return {"status": "success", "updated_events": results}

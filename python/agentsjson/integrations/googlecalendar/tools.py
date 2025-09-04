from pydantic import BaseModel
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build, Resource
from agentsjson.core.models.auth import OAuth2AuthConfig
from typing import Any, Dict
from functools import lru_cache

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
        credentials = Credentials(
            token=token,
            refresh_token=refresh_token,
            token_uri="https://oauth2.googleapis.com/token",
            scopes=scopes_str.split(",") if scopes_str else ["https://www.googleapis.com/auth/calendar"]
        )
        return build('calendar', 'v3', credentials=credentials)

    @staticmethod
    def _get_calendar_service(auth_config: OAuth2AuthConfig) -> Resource:
        """
        Retrieves a cached Google Calendar service using OAuth2 credentials.
        """
        scopes_str = ",".join(list(auth_config.scopes)) if auth_config.scopes else ""
        return Executor._build_service(auth_config.token, auth_config.refresh_token, scopes_str)

    @staticmethod
    def create_calendar(auth_config: OAuth2AuthConfig, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.calendars().insert(body=kwargs).execute()

    @staticmethod
    def delete_calendar(auth_config: OAuth2AuthConfig, calendarId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.calendars().delete(calendarId=calendarId).execute()

    @staticmethod
    def get_calendar_details(auth_config: OAuth2AuthConfig, calendarId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.calendars().get(calendarId=calendarId, **kwargs).execute()

    @staticmethod
    def list_calendars(auth_config: OAuth2AuthConfig, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.calendarList().list(**kwargs).execute()

    @staticmethod
    def update_calendar_settings(auth_config: OAuth2AuthConfig, calendarId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.calendars().update(calendarId=calendarId, body=kwargs).execute()

 
    @staticmethod
    def create_event(auth_config: OAuth2AuthConfig, calendarId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.events().insert(calendarId=calendarId, body=kwargs).execute()

    @staticmethod
    def delete_event(auth_config: OAuth2AuthConfig, calendarId: str, eventId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.events().delete(calendarId=calendarId, eventId=eventId).execute()

    @staticmethod
    def update_event(auth_config: OAuth2AuthConfig, calendarId: str, eventId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.events().update(calendarId=calendarId, eventId=eventId, body=kwargs).execute()

    @staticmethod
    def list_events(auth_config: OAuth2AuthConfig, calendarId: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        return service.events().list(calendarId=calendarId, **kwargs).execute()


    @staticmethod
    def add_attendee(auth_config: OAuth2AuthConfig, calendarId: str, eventId: str, attendeeEmail: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        event = service.events().get(calendarId=calendarId, eventId=eventId).execute()
        attendees = event.get("attendees", [])
        attendees.append({"email": attendeeEmail})
        event["attendees"] = attendees
        return service.events().update(calendarId=calendarId, eventId=eventId, body=event).execute()

    @staticmethod
    def remove_attendee(auth_config: OAuth2AuthConfig, calendarId: str, eventId: str, attendeeEmail: str, **kwargs):
        service = Executor._get_calendar_service(auth_config)
        event = service.events().get(calendarId=calendarId, eventId=eventId).execute()
        event["attendees"] = [a for a in event.get("attendees", []) if a["email"] != attendeeEmail]
        return service.events().update(calendarId=calendarId, eventId=eventId, body=event).execute()

    
    @staticmethod
    def check_free_busy(auth_config: OAuth2AuthConfig, **kwargs):
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
            result = Executor.delete_event(auth_config, calendarId, eventId)
            results.append(result)
        return {"status": "success", "deleted_events": results}

    @staticmethod
    def bulk_update_events(auth_config: OAuth2AuthConfig, calendarId: str, updates: list, **kwargs):
        results = []
        for update in updates:
            eventId = update.get("eventId")
            result = Executor.update_event(auth_config, calendarId, eventId, **update)
            results.append(result)
        return {"status": "success", "updated_events": results}

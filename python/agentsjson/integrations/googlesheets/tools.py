from pydantic import BaseModel
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build, Resource
from agentsjson.core.models.auth import OAuth2AuthConfig
from typing import ClassVar, Dict
from functools import lru_cache

class Executor(BaseModel):
    """
    Executor class for Google Sheets API operations.
    
    Authentication is handled via OAuth2AuthConfig which should include:
    - token: The OAuth 2.0 access token
    - refresh_token: The OAuth 2.0 refresh token (optional)
    - scopes: Set of OAuth 2.0 scopes (should include 'https://www.googleapis.com/auth/spreadsheets')
    """
    
    @staticmethod
    @lru_cache(maxsize=100)  # Cache up to 100 service instances
    def _build_service(token: str, refresh_token: str | None, scopes_str: str) -> Resource:
        """
        Creates a Google Sheets service using OAuth2 credentials.
        This function is cached with LRU policy.
        """
        credentials = Credentials(
            token=token,
            refresh_token=refresh_token,
            token_uri="https://oauth2.googleapis.com/token",
            scopes=scopes_str.split(",") if scopes_str else ["https://www.googleapis.com/auth/spreadsheets"]
        )
        return build('sheets', 'v4', credentials=credentials)

    @staticmethod
    def _get_sheets_service(auth_config: OAuth2AuthConfig) -> Resource:
        """
        Creates or retrieves a cached Google Sheets service using OAuth2 credentials.
        
        Args:
            auth_config: OAuth2AuthConfig containing the required OAuth2 credentials
        
        Returns:
            Google Sheets API service instance
        """
        # Convert scopes to a string for caching since lists aren't hashable
        scopes_str = ",".join(list(auth_config.scopes)) if auth_config.scopes else ""
        return Executor._build_service(auth_config.token, auth_config.refresh_token, scopes_str)

    @staticmethod
    def googlesheets_sheets_spreadsheets_create(auth_config: OAuth2AuthConfig, **kwargs):
        service = Executor._get_sheets_service(auth_config)
        return service.spreadsheets().create(body=kwargs).execute()

    @staticmethod
    def googlesheets_sheets_spreadsheets_get(auth_config: OAuth2AuthConfig, spreadsheetId: str, **kwargs):
        service = Executor._get_sheets_service(auth_config)
        return service.spreadsheets().get(spreadsheetId=spreadsheetId, **kwargs).execute()

    @staticmethod
    def googlesheets_sheets_spreadsheets_developer_metadata_get(auth_config: OAuth2AuthConfig, spreadsheetId: str, metadataId: str, **kwargs):
        service = Executor._get_sheets_service(auth_config)
        return service.spreadsheets().developerMetadata().get(
            spreadsheetId=spreadsheetId,
            metadataId=metadataId,
            **kwargs
        ).execute()

    @staticmethod
    def googlesheets_sheets_spreadsheets_developer_metadata_search(auth_config: OAuth2AuthConfig, spreadsheetId: str, **kwargs):
        service = Executor._get_sheets_service(auth_config)
        return service.spreadsheets().developerMetadata().search(
            spreadsheetId=spreadsheetId,
            **kwargs
        ).execute()

    @staticmethod
    def googlesheets_sheets_spreadsheets_sheets_copy_to(auth_config: OAuth2AuthConfig, spreadsheetId: str, sheetId: int, **kwargs):
        service = Executor._get_sheets_service(auth_config)
        return service.spreadsheets().sheets().copyTo(
            spreadsheetId=spreadsheetId,
            sheetId=sheetId,
            body=kwargs
        ).execute()

    @staticmethod
    def googlesheets_sheets_spreadsheets_values_get(auth_config: OAuth2AuthConfig, spreadsheetId: str, range: str, **kwargs):
        service = Executor._get_sheets_service(auth_config)
        return service.spreadsheets().values().get(
            spreadsheetId=spreadsheetId,
            range=range,
            **kwargs
        ).execute()

    @staticmethod
    def googlesheets_sheets_spreadsheets_values_update(auth_config: OAuth2AuthConfig, spreadsheetId: str, range: str, valueInputOption: str, **kwargs):
        service = Executor._get_sheets_service(auth_config)
        return service.spreadsheets().values().update(
            spreadsheetId=spreadsheetId,
            range=range,
            valueInputOption=valueInputOption,
            body=kwargs
        ).execute()

    @staticmethod
    def googlesheets_sheets_spreadsheets_values_append(auth_config: OAuth2AuthConfig, spreadsheetId: str, range: str, valueInputOption: str, **kwargs):
        service = Executor._get_sheets_service(auth_config)
        return service.spreadsheets().values().append(
            spreadsheetId=spreadsheetId,
            range=range,
            valueInputOption=valueInputOption,
            body=kwargs
        ).execute()

    @staticmethod
    def googlesheets_sheets_spreadsheets_values_clear(auth_config: OAuth2AuthConfig, spreadsheetId: str, range: str, **kwargs):
        service = Executor._get_sheets_service(auth_config)
        return service.spreadsheets().values().clear(
            spreadsheetId=spreadsheetId,
            range=range,
            **kwargs
        ).execute()

    @staticmethod
    def googlesheets_sheets_spreadsheets_values_batch_clear(auth_config: OAuth2AuthConfig, spreadsheetId: str, **kwargs):
        service = Executor._get_sheets_service(auth_config)
        return service.spreadsheets().values().batchClear(
            spreadsheetId=spreadsheetId,
            body=kwargs
        ).execute()

    @staticmethod
    def googlesheets_sheets_spreadsheets_values_batch_clear_by_data_filter(auth_config: OAuth2AuthConfig, spreadsheetId: str, **kwargs):
        service = Executor._get_sheets_service(auth_config)
        return service.spreadsheets().values().batchClearByDataFilter(
            spreadsheetId=spreadsheetId,
            body=kwargs
        ).execute()

    @staticmethod
    def googlesheets_sheets_spreadsheets_values_batch_get(auth_config: OAuth2AuthConfig, spreadsheetId: str, **kwargs):
        service = Executor._get_sheets_service(auth_config)
        return service.spreadsheets().values().batchGet(
            spreadsheetId=spreadsheetId,
            **kwargs
        ).execute()

    @staticmethod
    def googlesheets_sheets_spreadsheets_values_batch_get_by_data_filter(auth_config: OAuth2AuthConfig, spreadsheetId: str, **kwargs):
        service = Executor._get_sheets_service(auth_config)
        return service.spreadsheets().values().batchGetByDataFilter(
            spreadsheetId=spreadsheetId,
            body=kwargs
        ).execute()

    @staticmethod
    def googlesheets_sheets_spreadsheets_values_batch_update(auth_config: OAuth2AuthConfig, spreadsheetId: str, **kwargs):
        service = Executor._get_sheets_service(auth_config)
        return service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheetId,
            body=kwargs
        ).execute()

    @staticmethod
    def googlesheets_sheets_spreadsheets_values_batch_update_by_data_filter(auth_config: OAuth2AuthConfig, spreadsheetId: str, **kwargs):
        service = Executor._get_sheets_service(auth_config)
        return service.spreadsheets().values().batchUpdateByDataFilter(
            spreadsheetId=spreadsheetId,
            body=kwargs
        ).execute()

    @staticmethod
    def googlesheets_sheets_spreadsheets_batch_update(auth_config: OAuth2AuthConfig, spreadsheetId: str, **kwargs):
        service = Executor._get_sheets_service(auth_config)
        return service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheetId,
            body=kwargs
        ).execute()

    @staticmethod
    def googlesheets_sheets_spreadsheets_get_by_data_filter(auth_config: OAuth2AuthConfig, spreadsheetId: str, **kwargs):
        service = Executor._get_sheets_service(auth_config)
        return service.spreadsheets().getByDataFilter(
            spreadsheetId=spreadsheetId,
            body=kwargs
        ).execute()


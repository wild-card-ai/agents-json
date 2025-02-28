from pydantic import BaseModel
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build, Resource
from agentsjson.core.models.auth import OAuth2AuthConfig
from typing import ClassVar, Dict
from functools import lru_cache

class Executor(BaseModel):
    """
    Executor class for Google Docs API operations.
    
    Authentication is handled via OAuth2AuthConfig which should include:
    - token: The OAuth 2.0 access token
    - refresh_token: The OAuth 2.0 refresh token (optional)
    - scopes: Set of OAuth 2.0 scopes (should include 'https://www.googleapis.com/auth/documents')
    """
    
    @staticmethod
    @lru_cache(maxsize=100)  # Cache up to 100 service instances
    def _build_service(token: str, refresh_token: str | None, scopes_str: str) -> Resource:
        credentials = Credentials(
            token=token,
            refresh_token=refresh_token,
            token_uri="https://oauth2.googleapis.com/token",
            scopes=scopes_str.split(",") if scopes_str else ["https://www.googleapis.com/auth/documents"]
        )
        return build('docs', 'v1', credentials=credentials)

    @staticmethod
    def _get_docs_service(auth_config: OAuth2AuthConfig) -> Resource:
        scopes_str = ",".join(list(auth_config.scopes)) if auth_config.scopes else ""
        return Executor._build_service(auth_config.token, auth_config.refresh_token, scopes_str)

    @staticmethod
    def googledocs_create_document(auth_config: OAuth2AuthConfig, **kwargs) -> Dict:
        service = Executor._get_docs_service(auth_config)
        return service.documents().create(body=kwargs).execute()

    @staticmethod
    def googledocs_get_document(auth_config: OAuth2AuthConfig, documentId: str, **kwargs) -> Dict:
        service = Executor._get_docs_service(auth_config)
        return service.documents().get(documentId=documentId, **kwargs).execute()

    @staticmethod
    def googledocs_batch_update_documents(auth_config: OAuth2AuthConfig, documentId: str, **kwargs) -> Dict:
        service = Executor._get_docs_service(auth_config)
        return service.documents().batchUpdate(documentId=documentId, body=kwargs).execute()

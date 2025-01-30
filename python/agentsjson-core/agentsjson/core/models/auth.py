from enum import Enum
from typing import Literal, Optional, Set, Union
from typing_extensions import Annotated
from pydantic import BaseModel, Field

class AuthType(str, Enum):
    """Enumeration of supported authentication types."""
    BEARER = "bearer"
    API_KEY = "apiKey"
    BASIC = "basic"
    OAUTH2 = "oauth2"
    OAUTH1 = "oauth1"
    NONE = "none"

class BaseAuthConfig(BaseModel):
    """Base authentication configuration."""
    type: AuthType

class BearerAuthConfig(BaseAuthConfig):
    """Bearer token authentication configuration. To be added to header as 'Authorization: Bearer <token>' """
    type: Literal[AuthType.BEARER]
    token: str

class UserPassCredentials(BaseModel):
    username: str
    password: str
    base64_encode: bool = False

# Basic credentials can be either a string (base64 encoded credentials) or a UserPassCredentials object
BasicCredentials = Union[UserPassCredentials, str] 

class BasicAuthConfig(BaseAuthConfig):
    """Basic authentication configuration. To be added to header as 'Authorization: Basic <credentials>' """
    type: Literal[AuthType.BASIC]
    credentials: BasicCredentials
    
    
class OAuth1AuthConfig(BaseAuthConfig):
    """OAuth1 authentication configuration."""
    type: Literal[AuthType.OAUTH1]
    consumer_key: str
    consumer_secret: str
    access_token: str
    access_token_secret: str

class OAuth2AuthConfig(BaseAuthConfig):
    """OAuth2 authentication configuration."""
    type: Literal[AuthType.OAUTH2]
    token: str
    token_type: Optional[str] = None  # e.g., "Bearer"
    refresh_token: Optional[str] = None
    expires_at: Optional[int] = None  # Unix timestamp
    scopes: Optional[Set[str]] = None  # Scopes authorized for this key

class ApiKeyAuthConfig(BaseAuthConfig):
    """API key authentication configuration."""
    type: Literal[AuthType.API_KEY]
    key_value: str
    key_name: Optional[str] = None  # If the key name is different from the key value
    key_prefix: Optional[str] = None  # If the key prefix is different from the key value

# Union of all possible auth configurations using Pydantic's discriminated union
AuthConfig = Annotated[
    Union[BearerAuthConfig, ApiKeyAuthConfig, BasicAuthConfig, OAuth2AuthConfig, OAuth1AuthConfig],
    Field(discriminator='type')
]

# Helper class to build AuthConfig automatically
class AuthConfigBuilder(BaseModel):
    auth_config: AuthConfig

from typing import Any, Dict, Optional
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from agentsjson.core.models.auth import AuthConfig, AuthType, OAuth2AuthConfig, BearerAuthConfig, ApiKeyAuthConfig

class Executor:
    def __init__(self, client: Optional[WebClient] = None):
        self.client = client or WebClient()

    @staticmethod
    def _get_token(auth: AuthConfig) -> str:
        """Helper method to extract token from auth config"""
        if auth.type == AuthType.OAUTH2:
            return auth.token
        elif auth.type == AuthType.BEARER:
            return auth.token
        elif auth.type == AuthType.API_KEY:
            return auth.key_value
        else:
            raise ValueError(f"Unsupported auth type for Slack: {auth.type}")

    @staticmethod
    def _to_dict(response: Any) -> Dict[str, Any]:
        """Convert Slack response to a dictionary"""
        if hasattr(response, 'data'):
            return dict(response.data)
        elif hasattr(response, '__dict__'):
            return dict(response.__dict__)
        elif isinstance(response, dict):
            return response
        else:
            return {"response": str(response)}

    @staticmethod
    def chat_post_message(auth: AuthConfig, channel: str, text: str, **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.chat_postMessage(channel=channel, text=text, **kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def chat_update(auth: AuthConfig, channel: str, ts: str, text: str, **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.chat_update(channel=channel, ts=ts, text=text, **kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def chat_post_ephemeral(auth: AuthConfig, channel: str, user: str, text: str, **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.chat_postEphemeral(channel=channel, user=user, text=text, **kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def chat_delete(auth: AuthConfig, channel: str, ts: str, **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.chat_delete(channel=channel, ts=ts, **kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def conversations_history(auth: AuthConfig, channel: str, **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.conversations_history(channel=channel, **kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def conversations_info(auth: AuthConfig, channel: str, **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.conversations_info(channel=channel, **kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def conversations_list(auth: AuthConfig, **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        kwargs.pop('token', None)  # Remove token from kwargs if present
        response = client.conversations_list(**kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def conversations_open(auth: AuthConfig, users: str, **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.conversations_open(users=users.split(','), **kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def files_upload(auth: AuthConfig, file: str, filename: str, channels: str = "", **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.files_upload(file=file, filename=filename, channels=channels, **kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def files_info(auth: AuthConfig, file: str, **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.files_info(file=file, **kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def conversations_join(auth: AuthConfig, channel: str, **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.conversations_join(channel=channel, **kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def conversations_invite(auth: AuthConfig, channel: str, users: str, **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.conversations_invite(channel=channel, users=users.split(','), **kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def users_info(auth: AuthConfig, user: str, **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.users_info(user=user, **kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def search_messages(auth: AuthConfig, query: str, **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.search_messages(query=query, **kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def views_open(auth: AuthConfig, trigger_id: str, view: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.views_open(trigger_id=trigger_id, view=view, **kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def views_push(auth: AuthConfig, trigger_id: str, view: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.views_push(trigger_id=trigger_id, view=view, **kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def views_update(auth: AuthConfig, view_id: str, view: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.views_update(view_id=view_id, view=view, **kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def auth_test(auth: AuthConfig, **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.auth_test(**kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def reactions_add(auth: AuthConfig, channel: str, name: str, timestamp: str, **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.reactions_add(channel=channel, name=name, timestamp=timestamp, **kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def reactions_remove(auth: AuthConfig, channel: str, name: str, timestamp: str, **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.reactions_remove(channel=channel, name=name, timestamp=timestamp, **kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def pins_add(auth: AuthConfig, channel: str, timestamp: str, **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.pins_add(channel=channel, timestamp=timestamp, **kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def pins_list(auth: AuthConfig, channel: str, **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.pins_list(channel=channel, **kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def pins_remove(auth: AuthConfig, channel: str, timestamp: str, **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.pins_remove(channel=channel, timestamp=timestamp, **kwargs)
        return Executor._to_dict(response)

    @staticmethod
    def reminders_add(auth: AuthConfig, text: str, time: str, **kwargs) -> Dict[str, Any]:
        token = Executor._get_token(auth)
        client = WebClient(token=token)
        response = client.reminders_add(text=text, time=time, **kwargs)
        return Executor._to_dict(response)

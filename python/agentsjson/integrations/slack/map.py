from .tools import Executor
from ..types import ExecutorType

map_type = ExecutorType.SDK

map = {
    "slack_web_api_chat_post_message": Executor.chat_post_message,
    "slack_web_api_chat_update": Executor.chat_update,
    "slack_web_api_chat_post_ephemeral": Executor.chat_post_ephemeral,
    "slack_web_api_chat_delete": Executor.chat_delete,
    "slack_web_api_conversations_history": Executor.conversations_history,
    "slack_web_api_conversations_info": Executor.conversations_info,
    "slack_web_api_conversations_list": Executor.conversations_list,
    "slack_web_api_conversations_open": Executor.conversations_open,
    "slack_web_api_files_upload": Executor.files_upload,
    "slack_web_api_files_info": Executor.files_info,
    "slack_web_api_conversations_join": Executor.conversations_join,
    "slack_web_api_conversations_invite": Executor.conversations_invite,
    "slack_web_api_users_info": Executor.users_info,
    "slack_web_api_search_messages": Executor.search_messages,
    "slack_web_api_views_open": Executor.views_open,
    "slack_web_api_views_push": Executor.views_push,
    "slack_web_api_views_update": Executor.views_update,
    "slack_web_api_auth_test": Executor.auth_test,
    "slack_web_api_reactions_add": Executor.reactions_add,
    "slack_web_api_reactions_remove": Executor.reactions_remove,
    "slack_web_api_pins_add": Executor.pins_add,
    "slack_web_api_pins_list": Executor.pins_list,
    "slack_web_api_pins_remove": Executor.pins_remove,
    "slack_web_api_reminders_add": Executor.reminders_add
}

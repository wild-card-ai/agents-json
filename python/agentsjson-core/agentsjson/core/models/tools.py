from enum import Enum

class ToolFormat(str, Enum):
    """Enum representing different types of tools"""
    JSON = "json"
    OPENAI = "openai"

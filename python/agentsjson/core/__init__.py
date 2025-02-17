"""
Core functionality for Agents.json Python implementation.
"""

from .executor import execute, execute_flows
from .models.auth import AuthConfig, AuthType
from .models.bundle import Bundle
from .models.schema import AgentsJson, Flow, Link, Action
from .models.tools import ToolFormat
from .loader import load_agents_json
from .parsetools import flows_prompt, flows_tools
from .models.tools import ToolFormat  #for claude toolformat
# from .utils import conversion
from .parsetools import flow_to_claude_tool



__all__ = [
    'execute',
    'execute_flows',
    'AuthConfig',
    'AuthType',
    'Bundle',
    'AgentsJson',
    'Flow',
    'Link',
    'Action',
    'load_agents_json',
    'ToolFormat',
    'flows_prompt',
    'flows_tools'
    # 'flow_to_claude_tool'  # Expose flow_to_claude_tool for external use
]
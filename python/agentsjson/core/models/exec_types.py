from typing import Any, Dict, TypedDict
from dataclasses import dataclass

class ExecuteResult(TypedDict):
    small_responses: Dict[str, Any]
    large_responses: Dict[str, Any]

@dataclass
class ExecutorSettings:
    split_large_responses: bool = False  # Set to True to separate large responses for RAG
    size_threshold: int = 10 * 1024      # Size threshold in bytes (default 10 KB)

class ExecuteFlowsResult(TypedDict):
    results: Dict[str, Any]
    large_results: Dict[str, Any]

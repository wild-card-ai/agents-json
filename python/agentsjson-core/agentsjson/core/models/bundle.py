from .schema import AgentsJson
from typing import Dict, Any
from pydantic import BaseModel

class Bundle(BaseModel):
    """
    A Bundle represents a collection of API specifications and operations.

    Attributes:
        agentsjson: The parsed agents.json configuration containing flows, sources, and overrides
        openapi: The raw OpenAPI specification as a dictionary
        operations: A mapping of operation IDs to their OpenAPI info
    """
    agentsJson: AgentsJson
    openapi: Dict[str, Any]
    operations: Dict[str, Any]

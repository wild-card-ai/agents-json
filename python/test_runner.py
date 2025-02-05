#!/usr/bin/env python3

import os
import json
import yaml
import argparse
import logging
import time
import requests
from typing import Optional, Dict, Any, List
from pathlib import Path

from openai import OpenAI
import agentsjson.core as core
from agentsjson.core.models.bundle import Bundle
from agentsjson.core.models.auth import AuthType, AuthConfig, OAuth2AuthConfig, UserPassCredentials
from agentsjson.core import ToolFormat
from agentsjson.core.executor import execute_flows, configure_logging
from agentsjson.core.parsetools import configure_logging as configure_parsetools_logging

logger = logging.getLogger(__name__)

class OAuth2TokenRefreshError(Exception):
    """Raised when token refresh fails"""
    pass

class IntegrationTestRunner:
    def __init__(self, integration_name: str, openai_api_key: str, debug: bool = False):
        self.integration_name = integration_name
        self.openai_api_key = openai_api_key
        self.debug = debug
        self.bundle = None
        self.flows = None
        self.openai_client = OpenAI(api_key=openai_api_key)

        if debug:
            configure_logging(True)
            configure_parsetools_logging(True)

    def _fetch_openapi_spec(self, spec_path: str) -> Dict[str, Any]:
        """Fetch OpenAPI spec from local file or remote URL."""
        if spec_path.startswith('http'):
            response = requests.get(spec_path)
            response.raise_for_status()
            return yaml.safe_load(response.text)
        else:
            with open(spec_path, 'r') as f:
                return yaml.safe_load(f)

    def load_agents_json(self, agents_json_path: str) -> None:
        """Load the agents.json file and associated OpenAPI spec."""
        try:
            # Load agents.json content
            with open(agents_json_path, 'r') as f:
                agents_json_content = json.load(f)
                logger.debug(f"Loaded agents.json from {agents_json_path}")

            # Get the OpenAPI spec path from the sources
            source = agents_json_content['sources'][0]
            spec_path = source['path']
            
            # Load OpenAPI spec
            try:
                openapi_content = self._fetch_openapi_spec(spec_path)
                logger.debug(f"Loaded OpenAPI spec from {spec_path}")
            except Exception as e:
                logger.error(f"Failed to load OpenAPI spec from {spec_path}: {str(e)}")
                raise

            # Create the bundle structure
            bundle_data = {
                "agentsJson": agents_json_content,
                "openapi": openapi_content,
                "operations": {}
            }

            self.bundle = Bundle.model_validate(bundle_data)
            self.flows = self.bundle.agentsJson.flows
            logger.info("Successfully loaded agents.json and OpenAPI spec")

        except Exception as e:
            logger.error(f"Error loading agents.json: {str(e)}")
            raise

    def _validate_oauth2_config(self, auth_config: Dict[str, Any]) -> None:
        """Validate OAuth2 configuration."""
        required_fields = ['access_token']
        missing_fields = [field for field in required_fields if field not in auth_config]
        if missing_fields:
            raise ValueError(f"Missing required OAuth2 fields: {', '.join(missing_fields)}")

        # Validate token expiration if provided
        if 'expires_at' in auth_config:
            try:
                expires_at = int(auth_config['expires_at'])
                if expires_at < time.time():
                    logger.warning("OAuth2 token has expired")
                    if 'refresh_token' not in auth_config:
                        raise ValueError("Token has expired and no refresh token provided")
            except (ValueError, TypeError):
                raise ValueError("Invalid 'expires_at' value in OAuth2 config")

    def _create_auth_config(self, auth_config: Dict[str, Any]) -> AuthConfig:
        """Create an AuthConfig instance from the provided configuration."""
        auth_type = auth_config.get('type', 'api_key')
        
        if auth_type == 'api_key':
            if 'key' not in auth_config:
                raise ValueError("API key auth requires 'key' field")
            return AuthConfig(
                type=AuthType.API_KEY,
                key_value=auth_config['key']
            )
        elif auth_type == 'basic':
            if 'username' not in auth_config or 'password' not in auth_config:
                raise ValueError("Basic auth requires 'username' and 'password' fields")
            return AuthConfig(
                type=AuthType.BASIC,
                credentials=UserPassCredentials(
                    username=auth_config['username'],
                    password=auth_config['password']
                )
            )
        elif auth_type == 'oauth2':
            self._validate_oauth2_config(auth_config)
            return OAuth2AuthConfig(
                type=AuthType.OAUTH2,
                token=auth_config['access_token'],
                token_type=auth_config.get('token_type', 'Bearer'),
                refresh_token=auth_config.get('refresh_token'),
                expires_at=auth_config.get('expires_at'),
                scopes=set(auth_config.get('scopes', []))
            )
        else:
            raise ValueError(f"Unsupported auth type: {auth_type}")

    def execute_query(self, query: str, target_flow: Optional[str] = None, auth_config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute a natural language query against the integration."""
        if not self.bundle or not self.flows:
            raise Exception("Please call load_agents_json() first")

        # Filter flows if target_flow is specified
        flows = self.flows
        if target_flow:
            flows = [flow for flow in self.flows if flow.id == target_flow]
            if not flows:
                raise ValueError(f"Target flow '{target_flow}' not found")

        # Format flows for the prompt
        flows_context = core.flows_prompt(flows)

        # Create system prompt
        system_prompt = f"""You are an AI assistant that helps users interact with the {self.integration_name} API.
You have access to the following API flows:

{flows_context}

Analyze the user's request and use the appropriate API flows to accomplish the task.
You must give your arguments for the tool call as Structured Outputs JSON with keys `parameters` and `requestBody`
Call the tool with the arguments you provide.
"""

        logger.debug(f"System prompt: {system_prompt}")
        logger.debug(f"User query: {query}")

        # Get completion from OpenAI
        response = self.openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ],
            tools=core.flows_tools(flows, format=ToolFormat.OPENAI),
            temperature=0
        )

        # Configure auth based on the provided config
        if not auth_config:
            raise ValueError("auth_config is required")

        auth = self._create_auth_config(auth_config)

        # Execute the flows
        result = execute_flows(
            response,
            format=ToolFormat.OPENAI,
            bundle=self.bundle,
            flows=flows,
            auth=auth
        )

        return result

def main():
    parser = argparse.ArgumentParser(description='Test runner for agents.json integrations')
    parser.add_argument('integration', help='Name of the integration to test (e.g., hubspotcontacts)')
    parser.add_argument('query', help='Natural language query to execute')
    parser.add_argument('--flow', help='Target flow ID to execute (optional)')
    parser.add_argument('--auth-file', required=True, help='Path to auth config JSON file')
    parser.add_argument('--debug', action='store_true', help='Enable debug logging')
    
    args = parser.parse_args()

    # Setup logging
    if args.debug:
        configure_logging(True)
    
    try:
        # Load auth config
        with open(args.auth_file, 'r') as f:
            auth_config = json.load(f)

        # Get OpenAI API key from environment
        openai_api_key = os.getenv('OPENAI_API_KEY')
        if not openai_api_key:
            raise ValueError("OPENAI_API_KEY environment variable is required")

        # Initialize test runner
        runner = IntegrationTestRunner(args.integration, openai_api_key, args.debug)

        # Find agents.json file
        workspace_root = Path(__file__).parent.parent
        agents_json_path = workspace_root / 'agents_json' / args.integration / 'agents.json'
        
        if not agents_json_path.exists():
            raise FileNotFoundError(f"agents.json not found at {agents_json_path}")

        # Load agents.json
        runner.load_agents_json(str(agents_json_path))

        # Execute query
        result = runner.execute_query(args.query, args.flow, auth_config)

        # Print result
        print("\nExecution Result:")
        print(json.dumps(result, indent=2))

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        if args.debug:
            import traceback
            traceback.print_exc()
        exit(1)

if __name__ == '__main__':
    main() 
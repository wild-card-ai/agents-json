import json
import agentsjson.core as core
from agentsjson.core import load_agents_json, ToolFormat
from agentsjson.core.models.bundle import Bundle
from agentsjson.core.models.auth import AuthType, BearerAuthConfig

# API Keys (Replace with actual values)
STRIPE_API_KEY = "enter your key"
ANTHROPIC_API_KEY = "enter your claude key"

# Load Stripe's agents.json (API flows definition)
agents_json_url = "https://raw.githubusercontent.com/wild-card-ai/agents-json/refs/heads/master/agents_json/stripe/agents.json"
data: Bundle = core.load_agents_json(agents_json_url)
flows = data.agentsJson.flows

# Format flows for Claude prompt
flows_context = core.flows_prompt(flows)

# System prompt for Claude AI
system_prompt = f"""You are an AI assistant that helps users interact with the Stripe API.
You have access to the following API flows:

{flows_context}

Analyze the user's request and use the appropriate API flows to generate a structured response.
Your output should be JSON with 'parameters' and 'requestBody' fields.
"""

# Multiple Simulated Responses (Mimicking Claude's AI Output)
simulated_responses = [
    {
        "tool_call": {
            "name": "create_product_price",
            "parameters": {
                "product_name": "Tie Dye T-Shirt",
                "sizes": ["Small", "Medium", "Large"],
                "prices": [10, 15, 30]
            },
            "requestBody": {
                "description": "Tie Dye T-Shirts in three sizes: Small, Medium, and Large"
            }
        }
    },
    {
        "tool_call": {
            "name": "create_product_price",
            "parameters": {
                "product_name": "Hoodie",
                "sizes": ["S", "M", "L", "XL"],
                "prices": [25, 30, 35, 40]
            },
            "requestBody": {
                "description": "Comfortable hoodies available in various sizes"
            }
        }
    },
    {
        "tool_call": {
            "name": "update_product",
            "parameters": {
                "product_id": "prod_ABC123",
                "new_name": "Limited Edition Hoodie",
                "new_price": 50
            },
            "requestBody": {
                "description": "Updated pricing for Limited Edition Hoodie"
            }
        }
    },
    {
        "tool_call": {
            "name": "delete_product",
            "parameters": {
                "product_id": "prod_XYZ789"
            },
            "requestBody": {
                "description": "Removing old product from inventory"
            }
        }
    }
]

# Auth Configuration for Stripe API
auth = BearerAuthConfig(type=AuthType.BEARER, token=STRIPE_API_KEY)

# Function to execute simulated responses
def execute_simulated_flows(response, format, bundle, flows, auth):
    print("\nExecuting simulated response:")
    print(json.dumps(response, indent=2))

# Iterate through simulated responses and execute them
for response in simulated_responses:
    execute_simulated_flows(response, format=ToolFormat.ANTHROPIC, bundle=data, flows=flows, auth=auth)

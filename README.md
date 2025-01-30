<picture>
  <source srcset="./static/agentsjson-white-blackbackground.png">
  <img alt="Shows a white agents.json Logo with a black background." src="./static/agentsjson-white-blackbackground.png" width="full">
</picture>

<!-- [![GitHub stars](https://img.shields.io/github/stars/wild-card-ai/agents-json?style=social)](https://github.com/wild-card-ai/agents-json/stargazers) -->
[![Discord](https://img.shields.io/discord/1334616501436682405?style=flat&logo=discord&logoColor=white&label=discord&color=7289DA&link=https%3A%2F%2Fdiscord.gg%2F7AP6wSkVtQ)](https://discord.gg/7AP6wSkVtQ)
[![Documentation](https://img.shields.io/badge/Documentation-📕-blue)](https://docs.wild-card.ai/agents-json)
[![Twitter Follow](https://img.shields.io/twitter/follow/wildcard_ai?style=social)](https://x.com/wildcard_ai)

The agents.json Specification is an open specification that formally describes contracts for API and agent interactions, built on top of the OpenAPI standard.

The current version is 1.0.0.

The agents.json Bridge is a Python package that enables LLMs to load, parse, and run agents.json.

## Table of Contents
- [Python Quickstart](#python-quickstart)
- [Specification](#agentsjson-specification)
- [Feature Roadmap](#feature-roadmap)
- [Licenses](#licenses)
- [Contributions](#contributions)

## Python Quickstart

You can find the code for this example in [examples/single.ipynb](examples/single.ipynb).

### Setup

Install the agentsjson-core package and the openai package to create and run an agent:
```bash
pip install agentsjson
pip install openai
```

Load the agents.json file:
```python
agents_json_url = "https://raw.githubusercontent.com/wild-card-ai/agents-json/refs/heads/master/agents_json/stripe/agents.json"

from agentsjson.core.models import Flow
from agentsjson.core.models.bundle import Bundle
import agentsjson.core as core

# load the agents.json file
data: Bundle = core.load_agents_json(agents_json_url)
flows = data.agentsJson.flows
```

### Creating and Running an Agent
Set up your .env file with your API keys. We'll use Stripe for this agent.
```python
STRIPE_API_KEY="<your_stripe_api_key>"
OPENAI_API_KEY="<your_openai_api_key>"
```

Set up your agent:
```python
from agentsjson.core import ToolFormat

# Format the flows data for the prompt
flows_context = core.flows_prompt(flows)

# Create the system prompt
system_prompt = f"""You are an AI assistant that helps users interact with the Stripe API.
You have access to the following API flows:

{flows_context}

Analyze the user's request and use the appropriate API flows to accomplish the task.
You must give your arguments for the tool call as Structued Outputs JSON with keys `parameters` and `requestBody`"""
```

Configure authentication:
```python
from agentsjson.core.models.auth import AuthType, BearerAuthConfig
auth = BearerAuthConfig(type=AuthType.BEARER, token=STRIPE_API_KEY)
```

Run your agent:
```python
from openai import OpenAI
from agentsjson.core.executor import execute_flows
client = OpenAI(api_key=OPENAI_API_KEY)

query = "Create a new Stripe product for tie-die tshirts priced at $10, $15, and $30 for small, medium, and large sizes"

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": query}
    ],
    tools=core.flows_tools(flows, format=ToolFormat.OPENAI),
    temperature=0
)

response = execute_flows(response, format=core.ToolFormat.OPENAI, bundle=data, flows=flows, auth=auth)

response
```

For the full schema, see the [documentation 📕](https://docs.wild-card.ai/agentsjson/schema).

## agents.json Specification
The `agents.json` Specification is an open specification that formally describes contracts for API and agent interactions, built on top of the OpenAPI standard.

The current version is `1.0.0`.

Give feedback, share your projects, and get help in our [Discord](https://discord.gg/7AP6wSkVt).

### Schema

The full schema is available [here](https://docs.wild-card.ai/agentsjson/schema).

### Motivations

Enabling AI agents to interact with APIs is difficult. We faced the same problem as many others building agents: altering APIs to work reliably with LLMs and executing multiple API calls successfully in a row is a trial and error process.

APIs are designed for developers and not LLMs. If you're building integrations for AI agents, you need to write boilerplate, experiment with system prompts, optimize tool definitions, and parse responses into vector stores - for each API. 

For example, the Gmail API has endpoints to search for threads, list the emails in a thread, and reply with an email given base64 RFC 822 content. Instead, LLMs need a clear, top-level directive that can handle all of this with one tool.

**Why is `agents.json` built on OpenAPI?** — OpenAPI is the gold standard for describing how API endpoints work and can be executed. Most API providers have OpenAPI specs or have APIs that can be described fully by OpenAPI. These specs alone aren't sufficient for the age of AI agents, but provide great groundwork for API↔agent communication.

Agents need multiple context-specific API calls to complete their tasks. This is because APIs are resource-based, modifying objects, whereas agents are action-based, delivering outcomes. However, APIs alone lack enough information to deliver cohesive outcomes.

So we implemented `agents.json`, a schema to prescribe a set of API actions to an agent with the tools to make APIs work for LLMs. We built this for us and we're excited to share it with you.

## The agents.json File

`agents.json` is a JSON schema of structured contracts designed for AI agents. API providers use their existing OpenAPI spec to construct this file and agents inspect this file to run accurate series of API calls. 

The `agents.json` spec contains a set of additions to the OpenAPI spec - optimizing for endpoint discovery and LLM argument generation. These can include updating descriptions and adding examples.

Describing endpoints/data models without describing ***how*** they interact together is why AI agents struggle to take the right sequence of actions.

To solve this, we introduce flows and links. Flows are contracts with a series of 1 or more API calls that describe an outcome. Links describe how two actions are stitched together.

We propose the file placed in `/.well-known/agents.json` so it is easily discoverable by agents accessing web services. For now, we compose a GitHub repository as a registry for available `agents.json` files.

### The agents.json Bridge

The agents.json Bridge enables LLMs to load, parse, and run agents.json. Here's how it works:

1. A developer connects their agent with an agents.json file.
2. The relevant chain(s) are chosen by the agent and arguments populated for a given task.
3. The Bridge runs the chain(s).

The goal experience is a developer adds an agents.json file in their workflow and the correct set of actions for an integration is executed. The Bridge supports adding Basic, ApiKey, and Bearer authentication to requests.

### Design Tenets

1. **Build on top of the OpenAPI standard** <br>
   Leverage existing standards and infrastructure where possible.

2. **Prioritize open source** <br>
   Maintain trust, observability, and customizability.

3. **Optimize schema for LLMs, not humans** <br>
   Design with AI consumption in mind.

4. **Enforce Statelessness** <br>
   Orchestration is handled by the calling agent.

5. **Require minimal changes to existing APIs** <br>
   Make adoption as seamless as possible.

### Why Now?

With OpenAI's release of Operator, we've seen a paradigm shift in what AI will automate. Letting AI run free on the internet will ask for both features and guardrails to be built on web experiences for agents. Yet, for the majority of services - this is exactly the functionality APIs already provide - and more. 

Rather than just optimizing UXs for web agents - enriching APIs will create more scalable, powerful, and safe agents. APIs are supported by backend infrastructure built for scale. 

There are still open questions and more to be done. Starting the discussion now and building iteratively gives us a place to adapt alongside evolving paradigms in AI agent development. 

### FAQs

#### Shouldn't API providers provide their own agent servers or "/agent" endpoints?

We can begin building agents.json files immediately before official adoption by providers. No extra infrastructure changes, servers, or new endpoints. By putting responsibility of execution on the client - the paradigm abides by the same security and orchestration protocol of existing API based applications today. API providers can still choose to maintain official agents.json files.

#### Why route to an SDK instead of making HTTP requests directly?

Although OpenAPI specs offer great descriptions of how to use APIs, code-gen with tools like OpenAPI generator and Swagger code-gen isn't perfect. Many APIs have edge cases that are accounted for in client SDKs and not in raw HTTP requests. For example, Gmail's RFC2822 format or Twilio's custom TwiML format are better parsed by code rather than generated as input by an LLM. We include copies of OpenAPI specs beside agents.json files in the repo for use.

#### How is this different than the Model Context Protocol?

While MCP is designed to be stateful—relying on persistent connections between clients and servers for exchanging context and requests—Agents.json is stateless. Here, the agent independently manages all context. You can leverage your existing agent architecture and RAG systems to handle state effectively. Agents.json lets you build with existing pub/sub architectures, server-less environments, and infrastructure APIs already support today. And definitions are strongly typed by OpenAPI specs.

#### What about llms.txt?

[llms.txt](https://llmstxt.org) is a great standard for making website content more readable to LLMs, but it doesn't address the challenges of **taking structured actions**. While llms.txt helps LLMs retrieve and interpret information, agents.json enables them to execute multi-step workflows reliably.

#### Why use OpenAPI?

OpenAPI is a thoughtful standard that has evolved with the changes of HTTP APIs. It is the gold standard for describing how API endpoints work and can be executed. Most API providers have OpenAPI specs or have APIs that can be described fully by OpenAPI. These specs aren't quite sufficient for the age of agents, but do provide great groundwork for API↔agent communication.


## Feature Roadmap

- [ ] OAuth
- [ ] Memory & context management in links
- [ ] Transforming fields at runtime
- [ ] Rate-limits
- [ ] Parallel Tasking
- [ ] Conditionals
- [ ] Loops
- [ ] Failure Handling
- [ ] Streaming
- [ ] Pagination
- [ ] agents.json Interactive Builder
- [ ] agents.json Validator

## Licenses

The agents.json specification is open source, licensed under the [Apache 2.0 License](./agents_json/LICENSE).
The agents.json Bridge is source-available, licensed under the [BUSL-1.1 License](./python/LICENSE).

## Contributions

The agents.json specification needs community input. This GitHub repository hosts an informal overview, allowing for version control and public discussion. A community discord channel is available for sharing implementation experiences and discussing best practices. This is an evolving project and can't be done without your feedback.


## Team
This project is started by [Wildcard AI](https://wild-card.ai). We're a team of 2 founders, [Kaushik](https://x.com/kaushikm_) and [Yagnya](https://x.com/Life_of_Y_), wanting to make agents act predictably and safely.

<br>

<img width="full" align="center" src="./static/WildcardFoundersYC.jpg" alt="Wildcard AI Founders" width="100">

<br>

<div align="center">
Made with ❤️ in San Francisco


[![Discord](https://img.shields.io/discord/1334616501436682405?style=flat&logo=discord&logoColor=white&label=discord&color=7289DA&link=https%3A%2F%2Fdiscord.gg%2F7AP6wSkVtQ)](https://discord.gg/7AP6wSkVtQ)
[![Twitter Follow](https://img.shields.io/twitter/follow/wildcard_ai?style=social)](https://x.com/wildcard_ai)
[![Twitter Follow](https://img.shields.io/twitter/follow/kaushikm_?style=social)](https://x.com/kaushikm_)
[![Twitter Follow](https://img.shields.io/twitter/follow/Life_of_Y_?style=social)](https://x.com/Life_of_Y_)
</div> 




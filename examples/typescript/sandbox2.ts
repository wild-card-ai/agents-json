import { loadAgentsJson } from '../../typescript/src/core/loader';
import { AuthType, OAuth1AuthConfig, ApiKeyAuthConfig } from '../../typescript/src/types/auth';
import { executeFlows } from '../../typescript/src/core/executor';
import OpenAI from 'openai';
import type { ChatCompletionMessageParam, ChatCompletionTool } from 'openai/resources/chat';
import { OpenAIResponse } from '../../typescript/src/types/executor';
import { flowsTools, flowsPrompt } from '../../typescript/src/core/parsetools';
import { ToolFormat } from '../../typescript/src/types/tools';
import { Flow } from '../../typescript/src/types/schema';
import { Bundle } from '../../typescript/src/types/bundle';

// Configuration - these should be set in your environment
declare const process: {
  env: {
    TWITTER_CONSUMER_KEY: string;
    TWITTER_CONSUMER_SECRET: string;
    TWITTER_ACCESS_TOKEN: string;
    TWITTER_ACCESS_TOKEN_SECRET: string;
    GIPHY_API_KEY: string;
    OPENAI_API_KEY: string;
  };
  argv: string[];
};

const TWITTER_CONSUMER_KEY = process.env.TWITTER_CONSUMER_KEY;
const TWITTER_CONSUMER_SECRET = process.env.TWITTER_CONSUMER_SECRET;
const TWITTER_ACCESS_TOKEN = process.env.TWITTER_ACCESS_TOKEN;
const TWITTER_ACCESS_TOKEN_SECRET = process.env.TWITTER_ACCESS_TOKEN_SECRET;
const GIPHY_API_KEY = process.env.GIPHY_API_KEY;
const OPENAI_API_KEY = process.env.OPENAI_API_KEY;

const TWITTER_AGENTS_JSON_URL = 'https://raw.githubusercontent.com/wild-card-ai/agents-json/refs/heads/master/agents_json/twitter/agents.json';
const GIPHY_AGENTS_JSON_URL = 'https://raw.githubusercontent.com/wild-card-ai/agents-json/refs/heads/master/agents_json/giphy/agents.json';

type Agent = (userRequest: string) => Promise<Record<string, unknown>>;

interface AgentDefinition {
  name: string;
  agent: Agent;
  description: string;
}

async function createAgent(
  bundle: Bundle,
  flows: Flow[],
  systemPrompt: string,
  auth: OAuth1AuthConfig | ApiKeyAuthConfig
): Promise<Agent> {
  const openai = new OpenAI({ apiKey: OPENAI_API_KEY });

  return async (userRequest: string): Promise<Record<string, unknown>> => {
    const response = await openai.chat.completions.create({
      model: 'gpt-4o',
      messages: [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: userRequest }
      ],
      tools: flowsTools(flows, ToolFormat.OPENAI) as ChatCompletionTool[],
      tool_choice: 'auto'
    });

    return executeFlows(response as OpenAIResponse, bundle, flows, auth);
  };
}

async function createOrchestrator(agents: AgentDefinition[]) {
  const openai = new OpenAI({ apiKey: OPENAI_API_KEY });
  const agentsDescriptions = agents.map(a => `- ${a.name}: ${a.description}`).join('\n');

  const systemPrompt = `
You are a smart AI assistant that can help the user with their requests.
Break down the user's request into a list of sub-tasks and determine which agent to use and in what order to accomplish the task.
You have access to the following sub-agents with specialized capabilities:

${agentsDescriptions}

Use the appropriate sub-agent tool call to accomplish the task. 
Make sure to pass a precise natural language description of the task to the sub-agent. Pass the right context from the previous sub-agent's responses to the next sub-agent through the task.

You'll be given a response from the previous sub-agent. Use that response to determine the next sub-task and the agent to use.
If there's no more sub-tasks to accomplish, return the word STOP.
`;

  const agentTools: ChatCompletionTool[] = [{
    type: 'function',
    function: {
      name: 'execute_agent',
      description: 'This function is responsible for calling the appropriate agent to accomplish the task.',
      parameters: {
        type: 'object',
        properties: {
          agent_name: {
            type: 'string',
            enum: agents.map(a => a.name),
            description: 'The name of the agent to call.'
          },
          task: {
            type: 'string',
            description: 'The task to accomplish described precisely in natural language.'
          }
        },
        required: ['agent_name', 'task']
      }
    }
  }];

  async function orchestrate(messages: ChatCompletionMessageParam[]): Promise<unknown[]> {
    const response = await openai.chat.completions.create({
      model: 'gpt-4o',
      messages: [
        { role: 'system', content: systemPrompt },
        ...messages
      ],
      tools: agentTools,
      tool_choice: 'auto'
    });

    if (!response.choices[0].message.tool_calls) {
      return ['STOP'];
    }

    const responses: unknown[] = [];
    
    for (const toolCall of response.choices[0].message.tool_calls) {
      try {
        const args = JSON.parse(toolCall.function.arguments);
        const { task, agent_name } = args;

        const agent = agents.find(a => a.name === agent_name);
        if (agent) {
          const toolResponse = await agent.agent(task);
          responses.push(toolResponse);
        } else {
          throw new Error(`Agent ${agent_name} not found`);
        }
      } catch (error) {
        if (error instanceof Error) {
          throw new Error(`Invalid tool call arguments format: ${error.message}`);
        }
        throw error;
      }
    }

    const finalResponse = responses.length ? JSON.stringify(responses[responses.length - 1]) : 'STOP';

    if (finalResponse !== 'STOP') {
      const nextResponses = await orchestrate([...messages, { role: 'user', content: finalResponse }]);
      responses.push(...nextResponses);
    }

    return responses;
  }

  return orchestrate;
}

async function main() {
  try {
    const [twitterBundle, giphyBundle] = await Promise.all([
      loadAgentsJson(TWITTER_AGENTS_JSON_URL),
      loadAgentsJson(GIPHY_AGENTS_JSON_URL)
    ]);

    const twitterFlows = twitterBundle.agentsJson.flows;
    const giphyFlows = giphyBundle.agentsJson.flows;

    const twitterSystemPrompt = `You are an AI assistant that helps users interact with the Twitter API.
You have access to the following API flows:

${flowsPrompt(twitterFlows)}

Analyze the user's request and use the appropriate API flows to accomplish the task.
You must give your arguments for the tool call as Structured Outputs JSON with keys 'parameters' and 'requestBody'`;

    const giphySystemPrompt = `You are an AI assistant that helps users interact with the Giphy API.
You have access to the following API flows:

${flowsPrompt(giphyFlows)}

Analyze the user's request and call the corresponding tool call with the appropriate API flows to accomplish the task.
You must give your arguments for the tool call as Structured Outputs JSON with keys 'parameters' and 'requestBody'`;

    const twitterAuth: OAuth1AuthConfig = {
      type: AuthType.OAUTH1,
      consumer_key: TWITTER_CONSUMER_KEY,
      consumer_secret: TWITTER_CONSUMER_SECRET,
      access_token: TWITTER_ACCESS_TOKEN,
      access_token_secret: TWITTER_ACCESS_TOKEN_SECRET
    };

    const giphyAuth: ApiKeyAuthConfig = {
      type: AuthType.API_KEY,
      key_value: GIPHY_API_KEY,
      key_name: 'api_key',
      in: 'query'
    };

    const twitterAgent = await createAgent(twitterBundle, twitterFlows, twitterSystemPrompt, twitterAuth);
    const giphyAgent = await createAgent(giphyBundle, giphyFlows, giphySystemPrompt, giphyAuth);

    const agentsList: AgentDefinition[] = [
      {
        name: 'twitter_agent',
        agent: twitterAgent,
        description: 'This agent makes requests to the Twitter API.'
      },
      {
        name: 'giphy_agent',
        agent: giphyAgent,
        description: 'This agent makes requests to the Giphy API.'
      }
    ];

    const orchestrate = await createOrchestrator(agentsList);

    const query = 'find one random GIF of a cat that is funny and share it on twitter with the hashtag #agentsjson';
    await orchestrate([{ role: 'user', content: query }]);
  } catch (error) {
    console.error('Error:', error);
  }
}

if (import.meta.url === `file://${process.argv[1]}`) {
  main().catch(error => {
    console.error(error);
  });
} 
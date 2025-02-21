import { loadAgentsJson } from '../../typescript/src/core/loader';
import { AuthType, ApiKeyAuthConfig } from '../../typescript/src/types/auth';
import { executeFlows } from '../../typescript/src/core/executor';
import OpenAI from 'openai';
import type { ChatCompletionMessageParam, ChatCompletionTool } from 'openai/resources/chat';
import { OpenAIResponse } from '../../typescript/src/types/executor';
import { flowsTools } from '../../typescript/src/core/parsetools';
import { ToolFormat } from '../../typescript/src/types/tools';

async function main() {
  try {
    // Initialize OpenAI client
    const openai = new OpenAI({
      apiKey: process.env.OPENAI_API_KEY // Make sure to set this in your environment
    });

    // Load the agents.json bundle
    const bundle = await loadAgentsJson('https://raw.githubusercontent.com/wild-card-ai/agents-json/refs/heads/master/agents_json/resend/agents.json');

    // Set up Resend auth
    const auth: ApiKeyAuthConfig = {
      type: AuthType.API_KEY,
      key_value: process.env.RESEND_API_KEY || 'YOUR_RESEND_API_KEY', // Get from environment
      key_name: 'Authorization'
    };

    // Get flows from the bundle
    const flows = bundle.agentsJson.flows;

    // Create system prompt
    const systemPrompt = `You are a helpful assistant that can send emails using the Resend API. 
Available flows:
${flows.map(flow => `- ${flow.id}: ${flow.description}`).join('\n')}

Please help the user send emails by using the appropriate flow.`;

    // Create conversation with user query
    const messages: ChatCompletionMessageParam[] = [
      { role: 'system', content: systemPrompt },
      { role: 'user', content: 'Please send a test email to info@wild-card.ai with the subject "Test Email" from contact@hunly.io saying that this was sent from Typescript client' }
    ];

    // Call OpenAI
    const response = await openai.chat.completions.create({
      model: 'gpt-4o',
      messages,
      tools: flowsTools(flows, ToolFormat.OPENAI) as ChatCompletionTool[]
    });

    // Convert OpenAI response to our expected format
    const formattedResponse: OpenAIResponse = {
      choices: [{
        message: {
          content: response.choices[0].message.content || undefined,
          tool_calls: response.choices[0].message.tool_calls?.map(call => ({
            id: call.id,
            function: {
              name: call.function.name,
              arguments: call.function.arguments
            }
          }))
        }
      }]
    };

    // Execute the flows with the formatted OpenAI response
    const results = await executeFlows(
      formattedResponse,
      bundle,
      flows,
      auth
    );

  } catch (error) {
    console.error('Error:', error);
  }
}

// Check for required environment variables
if (!process.env.OPENAI_API_KEY) {
  console.error('Error: OPENAI_API_KEY environment variable is required');
  process.exit(1);
}

if (!process.env.RESEND_API_KEY) {
  console.error('Error: RESEND_API_KEY environment variable is required');
  process.exit(1);
}

main(); 
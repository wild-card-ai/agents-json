import { Agent } from '@mastra/core/agent';
import { openai } from '@ai-sdk/openai';
import { describe, it, expect } from 'vitest';
import { resendIntegration } from '.';
import { z } from 'zod';

describe('Resend Integration', () => {
  const API_KEY = process.env.RESEND_API_KEY;

  it('should execute integration methods', async () => {
    if (!API_KEY) {
      console.warn('Skipping Resend API tests - No API key provided');
      return;
    }

    const tools = resendIntegration.toTools();

    const sendEmailTool = tools.find(t => t.name === 'resend_sendEmail');
    expect(sendEmailTool).toBeDefined();
    expect(sendEmailTool?.name).toBe('resend_sendEmail');
    expect(sendEmailTool?.description).toBe('Sends an email via the Resend API');

    // Validate parameters is a Zod object
    expect(sendEmailTool?.parameters).toBeInstanceOf(z.ZodObject);

    // Send test email
    const sendResult = await sendEmailTool?.execute(
      { apiKey: API_KEY },
      {
        from: 'test@resend.dev',
        to: 'test@example.com',
        subject: 'Test Email',
        html: '<p>This is a test email</p>'
      }
    );
    expect(sendResult).toBeDefined();
    expect(sendResult).toHaveProperty('id');

    // Get email details
    const getEmailTool = tools.find(t => t.name === 'resend_getEmail');
    expect(getEmailTool).toBeDefined();
    expect(getEmailTool?.name).toBe('resend_getEmail');
    expect(getEmailTool?.description).toBe('Retrieves email details using the email\'s unique ID');

    const getResult = await getEmailTool?.execute(
      { apiKey: API_KEY },
      { id: sendResult.id }
    );
    expect(getResult).toBeDefined();
    expect(getResult).toHaveProperty('id', sendResult.id);
  });

  it('Add it to mastra', async () => {
    if (!API_KEY) {
      console.warn('Skipping Resend API tests - No API key provided');
      return;
    }

    const mastraTools = resendIntegration.toMastraTools({ apiKey: API_KEY });

    const agent = new Agent({
      name: 'Email Agent',
      instructions: 'You help users send emails. Use the sendEmail tool to send emails and the getEmail tool to check email status.',
      model: openai('gpt-4'),
      tools: mastraTools
    });

    // Test the agent with an email request
    const result = await agent.generate('Send a test email to test@example.com');
    console.log(result.text);
    expect(result).toBeDefined();
  }, 30000);
});

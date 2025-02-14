import { Agent } from '@mastra/core/agent';
import { openai } from '@ai-sdk/openai';
import { describe, it, expect } from 'vitest';
import { giphyIntegration } from '.';
import { z } from 'zod';

describe('Giphy Integration', () => {
  const API_KEY = process.env.GIPHY_API_KEY;

  it('should execute integration methods', async () => {
    if (!API_KEY) {
      console.warn('Skipping Giphy API tests - No API key provided');
      return;
    }

    const tools = giphyIntegration.toTools();

    const searchTool = tools.find(t => t.name === 'giphy_search');
    expect(searchTool).toBeDefined();
    expect(searchTool?.name).toBe('giphy_search');
    expect(searchTool?.description).toBe('Search for GIFs on Giphy');

    // Validate parameters is a Zod object
    expect(searchTool?.parameters).toBeInstanceOf(z.ZodObject);

    // Execute search
    const searchResult = await searchTool?.execute({ apiKey: API_KEY }, { query: 'test', limit: 1 });
    expect(searchResult).toBeDefined();
    expect(searchResult.data).toBeInstanceOf(Array);
    expect(searchResult.data[0]).toHaveProperty('id');
    expect(searchResult.data[0]).toHaveProperty('url');
    expect(searchResult.data[0]).toHaveProperty('title');
    expect(searchResult.data[0]).toHaveProperty('imageUrl');

    // Check trending tool
    const trendingTool = tools.find(t => t.name === 'giphy_trending');
    expect(trendingTool).toBeDefined();
    expect(trendingTool?.name).toBe('giphy_trending');
    expect(trendingTool?.description).toBe('Get trending GIFs');

    // Execute trending
    const trendingResult = await trendingTool?.execute({ apiKey: API_KEY }, { limit: 1 });
    expect(trendingResult).toBeDefined();
    expect(trendingResult.data).toBeInstanceOf(Array);
    expect(trendingResult.data[0]).toHaveProperty('id');
    expect(trendingResult.data[0]).toHaveProperty('url');
    expect(trendingResult.data[0]).toHaveProperty('title');
    expect(trendingResult.data[0]).toHaveProperty('imageUrl');
  });

  it('Add it to mastra', async () => {
    if (!API_KEY) {
      console.warn('Skipping Giphy API tests - No API key provided');
      return;
    }

    const mastraTools = giphyIntegration.toMastraTools({ apiKey: API_KEY });

    const agent = new Agent({
      name: 'Giphy Agent',
      instructions: 'You help users find and get GIFs. Use the search tool when users want specific GIFs, and the trending tool when they want to see what\'s popular.',
      model: openai('gpt-4'),
      tools: mastraTools
    });

    // Test the agent with a search query
    const result = await agent.generate('Find me a funny dragon gif');
    console.log(result.text);
    expect(result).toBeDefined();
  }, 30000);
});

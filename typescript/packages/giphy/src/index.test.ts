import { Agent } from '@agents-json/core';
import { openai } from '@ai-sdk/openai';
import { describe, it, expect } from 'vitest';
import { IntegrationRegistry } from '@agents-json/core';
import { giphyIntegration } from '.';
import { z } from 'zod';

describe('Integration Registry', () => {
  const API_KEY = process.env.GIPHY_API_KEY;

  const registry = new IntegrationRegistry();

  // Register the Giphy integration
  registry.register(giphyIntegration);

  // Get tool definitions
  const tools = registry.toTools();

  it('should register and execute integration methods', async () => {
    if (!API_KEY) {
      console.warn('Skipping Giphy API tests - No API key provided');
      return;
    }

    const searchTool = tools.find(t => t.name === 'giphy_search');
    expect(searchTool).toBeDefined();
    expect(searchTool?.name).toBe('giphy_search');
    expect(searchTool?.description).toBe('Search for GIFs on Giphy');

    // Validate parameters is a Zod object
    expect(searchTool?.parameters).toBeInstanceOf(z.ZodObject);

    // Test parameter validation
    const params = { query: 'test' };
    expect(() => searchTool?.parameters.parse(params)).not.toThrow();
    expect(() => searchTool?.parameters.parse({})).toThrow();

    // Execute search method
    const searchResult = await registry.execute('giphy', 'search',
      { apiKey: API_KEY },
      { query: 'cats', limit: 5 }
    );
    expect(searchResult.data).toBeDefined();
    expect(Array.isArray(searchResult.data)).toBe(true);
    expect(searchResult.data.length).toBeGreaterThan(0);
    expect(searchResult.data[0]).toHaveProperty('id');
    expect(searchResult.data[0]).toHaveProperty('url');
    expect(searchResult.data[0]).toHaveProperty('title');
    expect(searchResult.data[0]).toHaveProperty('imageUrl');

    // Execute trending method
    const trendingResult = await registry.execute('giphy', 'trending',
      { apiKey: API_KEY },
      { limit: 5, rating: 'g' }
    );
    expect(trendingResult.data).toBeDefined();
    expect(Array.isArray(trendingResult.data)).toBe(true);
    expect(trendingResult.data.length).toBeGreaterThan(0);
    expect(trendingResult.data[0]).toHaveProperty('id');
    expect(trendingResult.data[0]).toHaveProperty('url');
    expect(trendingResult.data[0]).toHaveProperty('title');
    expect(trendingResult.data[0]).toHaveProperty('imageUrl');
  });

  it('should return a map of tools with execute functions', async () => {
    if (!API_KEY) {
      console.warn('Skipping Giphy API tests - No API key provided');
      return;
    }

    const registry = new IntegrationRegistry();
    registry.register(giphyIntegration);

    const tools = registry.toTools();

    // Check search tool
    const searchTool = tools.find(t => t.name === 'giphy_search');
    expect(searchTool).toBeDefined();
    expect(searchTool?.name).toBe('giphy_search');
    expect(searchTool?.description).toBe('Search for GIFs on Giphy');

    // Validate parameters is a Zod object
    expect(searchTool?.parameters).toBeInstanceOf(z.ZodObject);

    // Test parameter validation
    const params = { query: 'test' };
    expect(() => searchTool?.parameters.parse(params)).not.toThrow();
    expect(() => searchTool?.parameters.parse({})).toThrow();

    // Test search execution
    const searchResult = await searchTool?.execute(
      { apiKey: API_KEY },
      { query: 'cats', limit: 5 }
    );

    console.log(searchResult);
    expect(searchResult.data).toBeDefined();
    expect(Array.isArray(searchResult.data)).toBe(true);
    expect(searchResult.data.length).toBeGreaterThan(0);
    expect(searchResult.data[0]).toHaveProperty('id');
    expect(searchResult.data[0]).toHaveProperty('url');
    expect(searchResult.data[0]).toHaveProperty('title');
    expect(searchResult.data[0]).toHaveProperty('imageUrl');

    // Check trending tool
    const trendingTool = tools.find(t => t.name === 'giphy_trending');
    expect(trendingTool).toBeDefined();
    expect(trendingTool?.name).toBe('giphy_trending');
    expect(trendingTool?.description).toBe('Get trending GIFs');

    // Test trending execution
    const trendingResult = await trendingTool?.execute(
      { apiKey: API_KEY },
      { limit: 5, rating: 'g' }
    );
    expect(trendingResult.data).toBeDefined();
    expect(Array.isArray(trendingResult.data)).toBe(true);
    expect(trendingResult.data.length).toBeGreaterThan(0);
    expect(trendingResult.data[0]).toHaveProperty('id');
    expect(trendingResult.data[0]).toHaveProperty('url');
    expect(trendingResult.data[0]).toHaveProperty('title');
    expect(trendingResult.data[0]).toHaveProperty('imageUrl');
  });

  it('should prevent duplicate integration registration', () => {
    const registry = new IntegrationRegistry();
    registry.register(giphyIntegration);
    expect(() => registry.register(giphyIntegration))
      .toThrow('Integration with id giphy already exists');
  });

  it('should throw error when executing non-existent method', async () => {
    const registry = new IntegrationRegistry();
    await expect(registry.execute('nonexistent', 'method', {}, {}))
      .rejects
      .toThrow('Method method not found in integration nonexistent');
  });


  it('Add it to mastra', async () => {
    if (!API_KEY) {
      console.warn('Skipping Giphy API tests - No API key provided');
      return;
    }

    const mastraTools = registry.toMastraTools({ apiKey: API_KEY });

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

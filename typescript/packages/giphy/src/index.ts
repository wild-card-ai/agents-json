import { Integration, IntegrationType, loadAgentsJson } from '@agents-json/core';
import path from 'path';

interface GiphyResponse {
  data: Array<{
    id: string;
    url: string;
    title: string;
    images: {
      original: {
        url: string;
      };
    };
  }>;
}

// Load and initialize the Giphy bundle
let giphyBundle: Awaited<ReturnType<typeof loadAgentsJson>> | null = null;

async function initGiphyBundle() {
  if (!giphyBundle) {
    const agentsJsonPath = path.resolve(__dirname, '../../../../agents_json/giphy/agents.json');
    giphyBundle = await loadAgentsJson({ url: agentsJsonPath });
  }
  return giphyBundle;
}

class GiphyExecutor {
  static async search(auth: Record<string, any>, params: Record<string, any>): Promise<any> {
    const bundle = await initGiphyBundle();
    if (!bundle) throw new Error('Failed to load Giphy bundle');

    const searchFlow = bundle.agentsJson.flows.find(f => f.id === 'search_gifs_flow');
    if (!searchFlow) throw new Error('Search flow not found in bundle');

    const searchAction = searchFlow.actions[0];
    const operation = bundle.operations[searchAction.operationId];
    if (!operation) throw new Error(`Operation ${searchAction.operationId} not found`);

    // Construct the request URL
    const baseUrl = bundle.openapi.servers[0].url;
    const path = '/v1' + operation.path;
    const url = new URL(path, baseUrl);

    // Add query parameters
    url.searchParams.append('api_key', auth.apiKey);
    url.searchParams.append('q', params.query);
    url.searchParams.append('limit', params.limit?.toString() || '10');
    if (params.offset) url.searchParams.append('offset', params.offset.toString());
    if (params.rating) url.searchParams.append('rating', params.rating);
    if (params.lang) url.searchParams.append('lang', params.lang);

    console.log(url);

    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Giphy API error: ${response.statusText}`);
    }
    const result = await response.json() as GiphyResponse;
    return {
      data: result.data.map(gif => ({
        id: gif.id,
        url: gif.url,
        title: gif.title,
        imageUrl: gif.images.original.url
      }))
    };
  }

  static async trending(auth: Record<string, any>, params: Record<string, any>): Promise<any> {
    const bundle = await initGiphyBundle();
    if (!bundle) throw new Error('Failed to load Giphy bundle');

    const trendingFlow = bundle.agentsJson.flows.find(f => f.id === 'get_trending_gifs_flow');
    if (!trendingFlow) throw new Error('Trending flow not found in bundle');

    const trendingAction = trendingFlow.actions[0];
    const operation = bundle.operations[trendingAction.operationId];
    if (!operation) throw new Error(`Operation ${trendingAction.operationId} not found`);

    // Construct the request URL
    const baseUrl = bundle.openapi.servers[0].url;
    const path = '/v1' + operation.path;
    const url = new URL(path, baseUrl);

    // Add query parameters
    url.searchParams.append('api_key', auth.apiKey);
    url.searchParams.append('limit', params.limit?.toString() || '10');
    if (params.offset) url.searchParams.append('offset', params.offset.toString());
    if (params.rating) url.searchParams.append('rating', params.rating);

    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Giphy API error: ${response.statusText}`);
    }
    const result = await response.json() as GiphyResponse;
    return {
      data: result.data.map(gif => ({
        id: gif.id,
        url: gif.url,
        title: gif.title,
        imageUrl: gif.images.original.url
      }))
    };
  }
}

export const giphyIntegration: Integration = {
  id: 'giphy',
  type: IntegrationType.SDK,
  methods: {
    search: {
      name: 'search',
      description: 'Search for GIFs on Giphy',
      type: IntegrationType.SDK,
      parameters: [
        {
          name: 'query',
          type: 'string',
          description: 'Search query string',
          required: true
        },
        {
          name: 'limit',
          type: 'number',
          description: 'Maximum number of objects to return. Default: 10',
          required: false
        },
        {
          name: 'offset',
          type: 'number',
          description: 'Offset into pagination',
          required: false
        },
        {
          name: 'rating',
          type: 'string',
          description: 'Filters results by specified rating',
          required: false
        },
        {
          name: 'lang',
          type: 'string',
          description: 'Specify language using ISO 639-1 language code',
          required: false
        }
      ],
      execute: GiphyExecutor.search
    },
    trending: {
      name: 'trending',
      description: 'Get trending GIFs',
      type: IntegrationType.SDK,
      parameters: [
        {
          name: 'limit',
          type: 'number',
          description: 'Maximum number of objects to return. Default: 10',
          required: false
        },
        {
          name: 'offset',
          type: 'number',
          description: 'Offset into pagination',
          required: false
        },
        {
          name: 'rating',
          type: 'string',
          description: 'Filters results by specified rating',
          required: false
        }
      ],
      execute: GiphyExecutor.trending
    }
  }
};

import { IntegrationType, createIntegration } from '@agents-json/core';

interface GiphyResponse {
  data: Array<{
    id: string;
    url: string;
    title: string;
    images: {
      original: {
        url: string;
      }
    }
  }>;
}

export const giphyIntegration = createIntegration({
  id: 'giphy',
  type: IntegrationType.REST,
  methods: {
    search: {
      name: 'search',
      description: 'Search for GIFs on Giphy',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'query',
          type: 'string',
          description: 'Search query',
          required: true
        },
        {
          name: 'limit',
          type: 'number',
          description: 'Maximum number of results',
          required: false
        }
      ],
      execute: async (auth: { apiKey: string }, params: { query: string; limit?: number }) => {
        const url = new URL('https://api.giphy.com/v1/gifs/search');
        url.searchParams.append('api_key', auth.apiKey);
        url.searchParams.append('q', params.query);
        url.searchParams.append('limit', String(params.limit || 1));

        const response = await fetch(url);
        if (!response.ok) {
          throw new Error(`Giphy API error: ${response.statusText}`);
        }

        const data: GiphyResponse = await response.json();
        return {
          data: data.data.map(gif => ({
            id: gif.id,
            url: gif.url,
            title: gif.title,
            imageUrl: gif.images.original.url
          }))
        };
      }
    },
    trending: {
      name: 'trending',
      description: 'Get trending GIFs',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'limit',
          type: 'number',
          description: 'Maximum number of results',
          required: false
        }
      ],
      execute: async (auth: { apiKey: string }, params: { limit?: number }) => {
        const url = new URL('https://api.giphy.com/v1/gifs/trending');
        url.searchParams.append('api_key', auth.apiKey);
        url.searchParams.append('limit', String(params.limit || 1));

        const response = await fetch(url);
        if (!response.ok) {
          throw new Error(`Giphy API error: ${response.statusText}`);
        }

        const data: GiphyResponse = await response.json();
        return {
          data: data.data.map(gif => ({
            id: gif.id,
            url: gif.url,
            title: gif.title,
            imageUrl: gif.images.original.url
          }))
        };
      }
    }
  },
});

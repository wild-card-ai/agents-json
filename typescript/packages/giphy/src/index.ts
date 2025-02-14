import { IntegrationType, createIntegration } from '@agents-json/core';

// Generic REST API handler
interface ExecuteRequestParams {
  apiKey: string;
  endpoint: string;
  searchParams?: Record<string, string>;
}

const executeRequest = async ({
  apiKey,
  endpoint,
  searchParams = {}
}: ExecuteRequestParams): Promise<any> => {
  const url = new URL(`https://api.giphy.com/v1/${endpoint}`);
  url.searchParams.append('api_key', apiKey);

  for (const [key, value] of Object.entries(searchParams)) {
    url.searchParams.append(key, value);
  }

  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Giphy API error: ${response.statusText}`);
  }

  return response.json();
};

export const giphyIntegration = createIntegration({
  id: 'giphy',
  type: IntegrationType.REST,
  methods: {
    searchGifs: {
      name: 'searchGifs',
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
        return executeRequest({
          apiKey: auth.apiKey,
          endpoint: 'gifs/search',
          searchParams: {
            q: params.query,
            limit: String(params.limit || 1)
          }
        });
      }
    },
    searchStickers: {
      name: 'searchStickers',
      description: 'Search for Stickers on Giphy',
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
        return executeRequest({
          apiKey: auth.apiKey,
          endpoint: 'stickers/search',
          searchParams: {
            q: params.query,
            limit: String(params.limit || 1)
          }
        });
      }
    },
    trendingGifs: {
      name: 'trendingGifs',
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
        return executeRequest({
          apiKey: auth.apiKey,
          endpoint: 'gifs/trending',
          searchParams: {
            limit: String(params.limit || 1)
          }
        });
      }
    },
    trendingStickers: {
      name: 'trendingStickers',
      description: 'Get trending Stickers',
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
        return executeRequest({
          apiKey: auth.apiKey,
          endpoint: 'stickers/trending',
          searchParams: {
            limit: String(params.limit || 1)
          }
        });
      }
    },
    translateGif: {
      name: 'translateGif',
      description: 'Translate text to a GIF',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'query',
          type: 'string',
          description: 'Text to translate',
          required: true
        }
      ],
      execute: async (auth: { apiKey: string }, params: { query: string }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          endpoint: 'gifs/translate',
          searchParams: {
            s: params.query
          }
        });
      }
    },
    translateSticker: {
      name: 'translateSticker',
      description: 'Translate text to a Sticker',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'query',
          type: 'string',
          description: 'Text to translate',
          required: true
        }
      ],
      execute: async (auth: { apiKey: string }, params: { query: string }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          endpoint: 'stickers/translate',
          searchParams: {
            s: params.query
          }
        });
      }
    },
    randomGif: {
      name: 'randomGif',
      description: 'Get a random GIF',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'tag',
          type: 'string',
          description: 'Tag to filter by',
          required: false
        }
      ],
      execute: async (auth: { apiKey: string }, params: { tag?: string }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          endpoint: 'gifs/random',
          searchParams: params.tag ? { tag: params.tag } : {}
        });
      }
    },
    randomSticker: {
      name: 'randomSticker',
      description: 'Get a random Sticker',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'tag',
          type: 'string',
          description: 'Tag to filter by',
          required: false
        }
      ],
      execute: async (auth: { apiKey: string }, params: { tag?: string }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          endpoint: 'stickers/random',
          searchParams: params.tag ? { tag: params.tag } : {}
        });
      }
    },
    getRandomId: {
      name: 'getRandomId',
      description: 'Get a random GIF ID',
      type: IntegrationType.REST,
      parameters: [],
      execute: async (auth: { apiKey: string }, params: {}) => {
        return executeRequest({
          apiKey: auth.apiKey,
          endpoint: 'randomid'
        });
      }
    },
    getEmoji: {
      name: 'getEmoji',
      description: 'Get Emoji GIFs',
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
        return executeRequest({
          apiKey: auth.apiKey,
          endpoint: 'emoji',
          searchParams: {
            limit: String(params.limit || 1)
          }
        });
      }
    },
    getEmojiVariations: {
      name: 'getEmojiVariations',
      description: 'Get variations of an Emoji GIF',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'gifId',
          type: 'string',
          description: 'GIF ID',
          required: true
        }
      ],
      execute: async (auth: { apiKey: string }, params: { gifId: string }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          endpoint: `emoji/${params.gifId}/variations`
        });
      }
    },
    getGifById: {
      name: 'getGifById',
      description: 'Get a GIF by ID',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'gifId',
          type: 'string',
          description: 'GIF ID',
          required: true
        }
      ],
      execute: async (auth: { apiKey: string }, params: { gifId: string }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          endpoint: `gifs/${params.gifId}`
        });
      }
    },
    getGifsByIds: {
      name: 'getGifsByIds',
      description: 'Get multiple GIFs by IDs',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'gifIds',
          type: 'string',
          description: 'Comma-separated GIF IDs',
          required: true
        }
      ],
      execute: async (auth: { apiKey: string }, params: { gifIds: string }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          endpoint: 'gifs',
          searchParams: {
            ids: params.gifIds
          }
        });
      }
    },
    getCategories: {
      name: 'getCategories',
      description: 'Get GIF categories',
      type: IntegrationType.REST,
      parameters: [],
      execute: async (auth: { apiKey: string }, params: {}) => {
        return executeRequest({
          apiKey: auth.apiKey,
          endpoint: 'gifs/categories'
        });
      }
    },
    searchTags: {
      name: 'searchTags',
      description: 'Search GIF tags',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'query',
          type: 'string',
          description: 'Search query',
          required: true
        }
      ],
      execute: async (auth: { apiKey: string }, params: { query: string }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          endpoint: 'gifs/search/tags',
          searchParams: {
            q: params.query
          }
        });
      }
    },
    searchChannels: {
      name: 'searchChannels',
      description: 'Search Giphy channels',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'query',
          type: 'string',
          description: 'Search query',
          required: true
        }
      ],
      execute: async (auth: { apiKey: string }, params: { query: string }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          endpoint: 'channels/search',
          searchParams: {
            q: params.query
          }
        });
      }
    },
    getRelatedTags: {
      name: 'getRelatedTags',
      description: 'Get tags related to a term',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'term',
          type: 'string',
          description: 'Term to get related tags for',
          required: true
        }
      ],
      execute: async (auth: { apiKey: string }, params: { term: string }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          endpoint: 'tags/related',
          searchParams: {
            term: params.term
          }
        });
      }
    },
    getTrendingSearches: {
      name: 'getTrendingSearches',
      description: 'Get trending searches',
      type: IntegrationType.REST,
      parameters: [],
      execute: async (auth: { apiKey: string }, params: {}) => {
        return executeRequest({
          apiKey: auth.apiKey,
          endpoint: 'trending/searches'
        });
      }
    }
  }
});

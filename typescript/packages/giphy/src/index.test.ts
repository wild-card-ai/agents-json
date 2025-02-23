import { describe, it, expect } from 'vitest';
import { map } from './map';

describe('Giphy Integration', () => {
  const API_KEY = process.env.GIPHY_API_KEY || '';

  const skipIfNoApiKey = () => {
    if (!API_KEY) {
      console.warn('Skipping Giphy API tests - No API key provided');
      return true;
    }
    return false;
  };

  // GIFs Tests
  it('should search gifs', async () => {
    if (skipIfNoApiKey()) return;

    const searchGifs = map['giphy_get_gifs_search'];
    const result = await searchGifs(API_KEY, { q: 'test', limit: 1 });

    expect(result).toBeDefined();
    expect(Array.isArray(result.data)).toBe(true);
    if (result.data.length > 0) {
      expect(result.data[0]).toHaveProperty('id');
      expect(result.data[0]).toHaveProperty('url');
      expect(result.data[0]).toHaveProperty('images');
    }
  });

  it('should get trending gifs', async () => {
    if (skipIfNoApiKey()) return;

    const trendingGifs = map['giphy_get_gifs_trending'];
    const result = await trendingGifs(API_KEY, { limit: 1 });

    expect(result).toBeDefined();
    expect(Array.isArray(result.data)).toBe(true);
    if (result.data.length > 0) {
      expect(result.data[0]).toHaveProperty('id');
      expect(result.data[0]).toHaveProperty('url');
      expect(result.data[0]).toHaveProperty('images');
    }
  });

  it('should get random gif', async () => {
    if (skipIfNoApiKey()) return;

    const randomGif = map['giphy_get_gifs_random'];
    const result = await randomGif(API_KEY);

    expect(result).toBeDefined();
    expect(result.data).toHaveProperty('id');
    expect(result.data).toHaveProperty('url');
    expect(result.data).toHaveProperty('images');
  });

  // Stickers Tests
  it('should search stickers', async () => {
    if (skipIfNoApiKey()) return;

    const searchStickers = map['giphy_get_stickers_search'];
    const result = await searchStickers(API_KEY, { q: 'test', limit: 1 });

    expect(result).toBeDefined();
    expect(Array.isArray(result.data)).toBe(true);
    if (result.data.length > 0) {
      expect(result.data[0]).toHaveProperty('id');
      expect(result.data[0]).toHaveProperty('url');
      expect(result.data[0]).toHaveProperty('images');
    }
  });

  it('should get trending stickers', async () => {
    if (skipIfNoApiKey()) return;

    const trendingStickers = map['giphy_get_stickers_trending'];
    const result = await trendingStickers(API_KEY, { limit: 1 });

    expect(result).toBeDefined();
    expect(Array.isArray(result.data)).toBe(true);
    if (result.data.length > 0) {
      expect(result.data[0]).toHaveProperty('id');
      expect(result.data[0]).toHaveProperty('url');
      expect(result.data[0]).toHaveProperty('images');
    }
  });

  // Categories and Tags Tests
  it('should get gif categories', async () => {
    if (skipIfNoApiKey()) return;

    const getCategories = map['giphy_get_gifs_categories'];
    const result = await getCategories(API_KEY, { limit: 1 });

    expect(result).toBeDefined();
    expect(result.data).toBeDefined();
  });

  it('should get related tags', async () => {
    if (skipIfNoApiKey()) return;

    const getRelatedTags = map['giphy_get_tags_related_by_term'];
    const result = await getRelatedTags(API_KEY, { term: 'fun' });

    expect(result).toBeDefined();
    expect(result.data).toBeDefined();
  });

  // Emoji Tests
  it('should get emoji', async () => {
    if (skipIfNoApiKey()) return;

    const getEmoji = map['giphy_get_emoji'];
    const result = await getEmoji(API_KEY);

    expect(result).toBeDefined();
    expect(result.data).toBeDefined();
  });

  // Other Tests
  it('should get trending searches', async () => {
    if (skipIfNoApiKey()) return;

    const getTrendingSearches = map['giphy_get_trending_searches'];
    const result = await getTrendingSearches(API_KEY);

    expect(result).toBeDefined();
    expect(result.data).toBeDefined();
  });
});

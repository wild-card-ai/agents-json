export class Configuration {
  constructor(public apiKey: string) { }
}

export interface GiphyResponse<T> {
  data: T;
  meta: {
    status: number;
    msg: string;
    response_id: string;
  };
  pagination?: {
    total_count: number;
    count: number;
    offset: number;
  };
}

export interface GiphyImage {
  url: string;
  width: string;
  height: string;
}

export interface GiphyGif {
  type: string;
  id: string;
  url: string;
  slug: string;
  bitly_gif_url: string;
  bitly_url: string;
  embed_url: string;
  username: string;
  source: string;
  title: string;
  rating: string;
  content_url: string;
  source_tld: string;
  source_post_url: string;
  import_datetime: string;
  trending_datetime: string;
  images: {
    original: GiphyImage;
    fixed_height: GiphyImage;
    fixed_width: GiphyImage;
    [key: string]: GiphyImage;
  };
}

export class DefaultApi {
  private readonly baseUrl = 'https://api.giphy.com';
  private readonly config: Configuration;

  constructor(config: Configuration) {
    this.config = config;
  }

  private async request<T>(endpoint: string, params: Record<string, any> = {}): Promise<GiphyResponse<T>> {
    const url = new URL(`${this.baseUrl}${endpoint}`, 'https://api.giphy.com');
    url.searchParams.append('api_key', this.config.apiKey);

    for (const [key, value] of Object.entries(params)) {
      if (value !== undefined) {
        url.searchParams.append(key, String(value));
      }
    }

    console.log('Making request to:', url.toString());
    const response = await fetch(url.toString());
    if (!response.ok) {
      const errorText = await response.text();
      console.error('Error response:', errorText);
      throw new Error(`${response.status} ${response.statusText}: ${errorText}`);
    }

    return response.json();
  }

  // GIFs Endpoints
  async giphy_get_gifs_trending(params: {
    limit?: number;
    offset?: number;
    rating?: string;
    random_id?: string;
  } = {}): Promise<GiphyResponse<GiphyGif[]>> {
    return this.request<GiphyGif[]>('/v1/gifs/trending', params);
  }

  async giphy_get_gifs_search(params: {
    q: string;
    limit?: number;
    offset?: number;
    rating?: string;
    lang?: string;
    random_id?: string;
  }): Promise<GiphyResponse<GiphyGif[]>> {
    return this.request<GiphyGif[]>('/v1/gifs/search', params);
  }

  async giphy_get_gifs_random(params: {
    tag?: string;
    rating?: string;
    random_id?: string;
  } = {}): Promise<GiphyResponse<GiphyGif>> {
    return this.request<GiphyGif>('/v1/gifs/random', params);
  }

  async giphy_get_gifs_by_gif_id(params: {
    gif_id: string;
  }): Promise<GiphyResponse<GiphyGif>> {
    return this.request<GiphyGif>(`/v1/gifs/${params.gif_id}`, {});
  }

  async giphy_get_gifs(params: {
    ids: string[];
  }): Promise<GiphyResponse<GiphyGif[]>> {
    return this.request<GiphyGif[]>('/v1/gifs', { ids: params.ids.join(',') });
  }

  // Stickers Endpoints
  async giphy_get_stickers_trending(params: {
    limit?: number;
    offset?: number;
    rating?: string;
    random_id?: string;
  } = {}): Promise<GiphyResponse<GiphyGif[]>> {
    return this.request<GiphyGif[]>('/v1/stickers/trending', params);
  }

  async giphy_get_stickers_search(params: {
    q: string;
    limit?: number;
    offset?: number;
    rating?: string;
    lang?: string;
    random_id?: string;
  }): Promise<GiphyResponse<GiphyGif[]>> {
    return this.request<GiphyGif[]>('/v1/stickers/search', params);
  }

  async giphy_get_stickers_random(params: {
    tag?: string;
    rating?: string;
    random_id?: string;
  } = {}): Promise<GiphyResponse<GiphyGif>> {
    return this.request<GiphyGif>('/v1/stickers/random', params);
  }

  async giphy_get_stickers_translate(params: {
    s: string;
    rating?: string;
  }): Promise<GiphyResponse<GiphyGif>> {
    return this.request<GiphyGif>('/v1/stickers/translate', params);
  }

  // Categories and Tags
  async giphy_get_gifs_categories(params: {
    limit?: number;
    offset?: number;
  } = {}): Promise<GiphyResponse<any>> {
    return this.request('/v1/gifs/categories', params);
  }

  async giphy_get_gifs_search_tags(params: {
    q: string;
    limit?: number;
    offset?: number;
  }): Promise<GiphyResponse<any>> {
    return this.request('/v1/gifs/search/tags', params);
  }

  async giphy_get_tags_related_by_term(params: {
    term: string;
  }): Promise<GiphyResponse<any>> {
    return this.request('/v1/tags/related/' + encodeURIComponent(params.term), {});
  }

  // Emoji Endpoints
  async giphy_get_emoji(params: Record<string, any> = {}): Promise<GiphyResponse<any>> {
    return this.request('/v1/emoji', params);
  }

  async giphy_get_emoji_variations_by_gif_id(params: {
    gif_id: string;
  }): Promise<GiphyResponse<any>> {
    return this.request(`/v1/emoji/${params.gif_id}`, {});
  }

  // Channel Endpoints
  async giphy_get_channels_search(params: {
    q: string;
    limit?: number;
    offset?: number;
  }): Promise<GiphyResponse<any>> {
    return this.request('/v1/channels/search', params);
  }

  // Other Endpoints
  async giphy_get_randomid(): Promise<GiphyResponse<any>> {
    return this.request('/v1/randomid', {});
  }

  async giphy_get_trending_searches(): Promise<GiphyResponse<any>> {
    return this.request('/v1/trending/searches', {});
  }
}

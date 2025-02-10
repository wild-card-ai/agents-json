import axios, { AxiosInstance, AxiosRequestConfig, Method } from 'axios';
import { AuthConfig, AuthType, OAuth1AuthConfig, OAuth2AuthConfig } from '../types/auth';
import OAuth from 'oauth-1.0a';
import crypto from 'crypto';

export interface RestApiConfig {
  baseURL: string;
  headers?: Record<string, string>;
}

export interface RestApiRequest {
  method: Method;
  path: string;
  pathParams?: Record<string, string>;
  parameters?: Record<string, unknown>;
  requestBody?: Record<string, unknown>;
  headers?: Record<string, string>;
}

/**
 * Replaces path parameters in the format :paramName with their values
 * Example: replacePath('/users/:userId/posts/:postId', { userId: '123', postId: '456' })
 * Returns: '/users/123/posts/456'
 */
function replacePath(path: string, params?: Record<string, string>): string {
  if (!params) return path;
  return path.replace(/:([a-zA-Z][a-zA-Z0-9_]*)/g, (_, key) => {
    const value = params[key];
    if (value === undefined) {
      throw new Error(`Missing required path parameter: ${key}`);
    }
    return encodeURIComponent(value);
  });
}

export class RestApiHandler {
  private client: AxiosInstance;
  private auth?: AuthConfig;

  constructor(config: RestApiConfig) {
    this.client = axios.create({
      baseURL: config.baseURL,
      headers: {
        'Content-Type': 'application/json',
        ...config.headers,
      },
    });
  }

  setAuth(auth: AuthConfig): void {
    this.auth = auth;
  }

  private getAuthHeaders(): Record<string, string> {
    if (!this.auth) {
      return {};
    }
    
    switch (this.auth.type) {
      case AuthType.API_KEY: {
        if (this.auth.in !== 'query') {
          return { [this.auth.key_name || 'X-API-Key']: this.auth.key_value };
        }
        return {};
      }
      case AuthType.BEARER: {
        return { Authorization: `Bearer ${this.auth.token}` };
      }
      case AuthType.BASIC: {
        let auth: string;
        if (typeof this.auth.credentials === 'string') {
          auth = Buffer.from(this.auth.credentials).toString('base64');
        } else {
          const { username, password } = this.auth.credentials;
          auth = Buffer.from(`${username}:${password}`).toString('base64');
        }
        return { Authorization: `Basic ${auth}` };
      }
      case AuthType.OAUTH1:
        return {};
      case AuthType.OAUTH2: {
        return { Authorization: `Bearer ${(this.auth as OAuth2AuthConfig).token}` };
      }
      default:
        return {};
    }
  }

  private async handleOAuth1Request(
    request: RestApiRequest,
    auth: OAuth1AuthConfig
  ): Promise<Record<string, unknown>> {
    const oauth = new OAuth({
      consumer: {
        key: auth.consumer_key,
        secret: auth.consumer_secret,
      },
      signature_method: 'HMAC-SHA1',
      hash_function(baseString: string, key: string) {
        return crypto
          .createHmac('sha1', key)
          .update(baseString)
          .digest('base64');
      },
    });

    const url = new URL(request.path, this.client.defaults.baseURL).toString();
    const requestData = {
      url,
      method: request.method,
      data: request.parameters || {},
    };

    const oauthHeaders = oauth.toHeader(
      oauth.authorize(requestData, {
        key: auth.access_token,
        secret: auth.access_token_secret,
      })
    );

    const config: AxiosRequestConfig = {
      method: request.method,
      url: request.path,
      params: request.parameters,
      data: request.requestBody,
      headers: {
        ...oauthHeaders,
        ...request.headers,
        'Content-Type': 'application/json',
      },
    };

    try {
      const response = await this.client.request(config);
      return response.data;
    } catch (error) {
      if (axios.isAxiosError(error)) {
        throw new Error(
          `OAuth1 API request failed: ${error.response?.status} ${error.response?.statusText}\n${JSON.stringify(
            error.response?.data,
            null,
            2
          )}`
        );
      }
      throw error;
    }
  }

  async request(request: RestApiRequest): Promise<Record<string, unknown>> {
    if (this.auth?.type === AuthType.OAUTH1) {
      return this.handleOAuth1Request(request, this.auth as OAuth1AuthConfig);
    }

    const resolvedPath = replacePath(request.path, request.pathParams);
    const authHeaders = this.getAuthHeaders();

    let params = { ...request.parameters };
    if (this.auth?.type === AuthType.API_KEY && this.auth.in === 'query') {
      params = {
        ...params,
        [this.auth.key_name || 'api_key']: this.auth.key_value
      };
    }

    const config: AxiosRequestConfig = {
      method: request.method,
      url: resolvedPath,
      params,
      data: request.requestBody,
      headers: {
        ...authHeaders,
        ...request.headers,
      },
    };

    try {
      const response = await this.client.request(config);
      return response.data;
    } catch (error) {
      if (axios.isAxiosError(error)) {
        throw new Error(
          `API request failed: ${error.response?.status} ${error.response?.statusText}\n${JSON.stringify(
            error.response?.data,
            null,
            2
          )}`
        );
      }
      throw error;
    }
  }

  async get(
    path: string,
    parameters?: Record<string, unknown>,
    pathParams?: Record<string, string>
  ): Promise<Record<string, unknown>> {
    return this.request({
      method: 'GET',
      path,
      parameters,
      pathParams,
    });
  }

  async post(
    path: string,
    requestBody?: Record<string, unknown>,
    parameters?: Record<string, unknown>,
    pathParams?: Record<string, string>
  ): Promise<Record<string, unknown>> {
    return this.request({
      method: 'POST',
      path,
      parameters,
      requestBody,
      pathParams,
    });
  }

  async put(
    path: string,
    requestBody?: Record<string, unknown>,
    parameters?: Record<string, unknown>,
    pathParams?: Record<string, string>
  ): Promise<Record<string, unknown>> {
    return this.request({
      method: 'PUT',
      path,
      parameters,
      requestBody,
      pathParams,
    });
  }

  async patch(
    path: string,
    requestBody?: Record<string, unknown>,
    parameters?: Record<string, unknown>,
    pathParams?: Record<string, string>
  ): Promise<Record<string, unknown>> {
    return this.request({
      method: 'PATCH',
      path,
      parameters,
      requestBody,
      pathParams,
    });
  }

  async delete(
    path: string,
    parameters?: Record<string, unknown>,
    pathParams?: Record<string, string>
  ): Promise<Record<string, unknown>> {
    return this.request({
      method: 'DELETE',
      path,
      parameters,
      pathParams,
    });
  }
} 
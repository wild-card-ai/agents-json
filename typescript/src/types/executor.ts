import { AuthConfig, OAuth1AuthConfig, OAuth2AuthConfig, ApiKeyAuthConfig } from './auth';
import { ExecutorType } from './tools';

export interface ExecutionTrace {
  [key: string]: {
    parameters?: Record<string, unknown>;
    requestBody?: Record<string, unknown>;
    responses?: Record<string, unknown>;
  };
}

export type ExecuteResult = Record<string, unknown>;

export interface OpenAIToolCall {
  id: string;
  function: {
    name: string;
    arguments: string;
  };
}

export interface OpenAIResponse {
  choices: Array<{
    message: {
      tool_calls?: OpenAIToolCall[];
      content?: string;
    };
  }>;
}

export type AuthResult = string | [string, string] | OAuth1AuthConfig | OAuth2AuthConfig | ApiKeyAuthConfig;

export interface IntegrationModule {
  mapType: ExecutorType;
  map: Record<string, (
    auth: AuthResult | AuthConfig, 
    params: Record<string, unknown>,
    body?: Record<string, unknown>
  ) => Promise<unknown>>;
} 
// Translated from Python Pydantic models to TypeScript interfaces and classes

export enum AuthType {
    BEARER = "bearer",
    API_KEY = "apiKey",
    BASIC = "basic",
    OAUTH2 = "oauth2",
    OAUTH1 = "oauth1",
    NONE = "none",
  }
  
  /** Base authentication configuration. */
  export interface BaseAuthConfig {
    type: AuthType;
  }
  
  /** Bearer token authentication configuration.
   * To be added to header as 'Authorization: Bearer <token>'
   */
  export interface BearerAuthConfig extends BaseAuthConfig {
    type: AuthType.BEARER;
    token: string;
  }
  
  /** User credentials with optional base64 encoding. */
  export interface UserPassCredentials {
    username: string;
    password: string;
    base64_encode?: boolean;
  }
  
  /** Basic credentials can be either a string (base64 encoded credentials) or a UserPassCredentials object */
  export type BasicCredentials = UserPassCredentials | string;
  
  /** Basic authentication configuration.
   * To be added to header as 'Authorization: Basic <credentials>'
   */
  export interface BasicAuthConfig extends BaseAuthConfig {
    type: AuthType.BASIC;
    credentials: BasicCredentials;
  }
  
  /** OAuth1 authentication configuration. */
  export interface OAuth1AuthConfig extends BaseAuthConfig {
    type: AuthType.OAUTH1;
    consumer_key: string;
    consumer_secret: string;
    access_token: string;
    access_token_secret: string;
  }
  
  /** OAuth2 authentication configuration. */
  export interface OAuth2AuthConfig extends BaseAuthConfig {
    type: AuthType.OAUTH2;
    token: string;
    token_type?: string; // e.g., "Bearer"
    refresh_token?: string;
    expires_at?: number; // Unix timestamp
    scopes?: Set<string>; // Scopes authorized for this key
  }
  
  /** API key authentication configuration.
   * Can be added to headers or query parameters
   */
  export interface ApiKeyAuthConfig extends BaseAuthConfig {
    type: AuthType.API_KEY;
    key_value: string;
    key_name?: string;  // If the key name is different from the key value
    in?: 'header' | 'query';  // Where to put the API key, defaults to header
  }
  
  /** Union of all possible auth configurations */
  export type AuthConfig =
    | BearerAuthConfig
    | ApiKeyAuthConfig
    | BasicAuthConfig
    | OAuth2AuthConfig
    | OAuth1AuthConfig;
  
  /** Helper class to build AuthConfig automatically */
  export class AuthConfigBuilder {
    auth_config: AuthConfig;
  
    constructor(auth_config: AuthConfig) {
      this.auth_config = auth_config;
    }
  
    // You can add methods here to manipulate auth_config if needed
  }
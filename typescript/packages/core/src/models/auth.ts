import { z } from 'zod';

export enum AuthType {
  API_KEY = 'api_key',
  BEARER = 'bearer',
  BASIC = 'basic',
  OAUTH1 = 'oauth1',
  OAUTH2 = 'oauth2'
}

export const UserPassCredentialsSchema = z.object({
  username: z.string(),
  password: z.string()
});

export type UserPassCredentials = z.infer<typeof UserPassCredentialsSchema>;

export const OAuth1AuthConfigSchema = z.object({
  type: z.literal(AuthType.OAUTH1),
  consumerKey: z.string(),
  consumerSecret: z.string(),
  accessToken: z.string(),
  tokenSecret: z.string()
});

export type OAuth1AuthConfig = z.infer<typeof OAuth1AuthConfigSchema>;

export const OAuth2AuthConfigSchema = z.object({
  type: z.literal(AuthType.OAUTH2),
  clientId: z.string(),
  clientSecret: z.string(),
  accessToken: z.string(),
  refreshToken: z.string().optional()
});

export type OAuth2AuthConfig = z.infer<typeof OAuth2AuthConfigSchema>;

export const ApiKeyAuthConfigSchema = z.object({
  type: z.literal(AuthType.API_KEY),
  keyValue: z.string()
});

export const BearerAuthConfigSchema = z.object({
  type: z.literal(AuthType.BEARER),
  token: z.string()
});

export const BasicAuthConfigSchema = z.object({
  type: z.literal(AuthType.BASIC),
  credentials: z.union([UserPassCredentialsSchema, z.string()])
});

export const AuthConfigSchema = z.discriminatedUnion('type', [
  ApiKeyAuthConfigSchema,
  BearerAuthConfigSchema,
  BasicAuthConfigSchema,
  OAuth1AuthConfigSchema,
  OAuth2AuthConfigSchema
]);

export type AuthConfig = z.infer<typeof AuthConfigSchema>;

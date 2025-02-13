import { ExecutorType } from '../types/tools';
import { RestApiHandler, RestApiConfig } from '../core/rest-api-handler';
import { createApiMap, PathDefinition, RequestConfig } from './api-map-generator';
import { Method } from 'axios';
import { AuthConfig } from '../types/auth';
import { Bundle } from '../types/bundle';
import { IntegrationModule, AuthResult } from '../types/executor';

export interface ApiIntegrationConfig extends Omit<RestApiConfig, 'baseURL'> {
  auth?: AuthConfig;
}

export async function initApiIntegration(bundle: Bundle, config: ApiIntegrationConfig): Promise<IntegrationModule> {
  // Initialize the REST API handler with baseURL from the bundle
  const api = new RestApiHandler({
    ...config,
    baseURL: bundle.baseURL
  });

  // Convert operations to path definitions
  const paths: PathDefinition[] = Object.entries(bundle.operations).map(([operationId, operation]) => {
    const op = operation as Record<string, unknown>;
    const method = (op.method as string).toUpperCase();
    if (!['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'].includes(method)) {
      throw new Error(`Invalid HTTP method: ${method}`);
    }
    return {
      path: op.path as string,
      method: method as Method,
      operationId,
    };
  });

  // Create the API map with the correct auth type
  const apiMap = createApiMap(api, paths);
  const map: Record<string, (
    auth: AuthResult | AuthConfig, 
    params: Record<string, unknown>,
    body?: Record<string, unknown>
  ) => Promise<unknown>> = {};
  
  // Convert each API function to match the expected signature
  for (const [key, func] of Object.entries(apiMap)) {
    map[key] = async (
      auth: AuthResult | AuthConfig, 
      params: Record<string, unknown>,
      body?: Record<string, unknown>
    ) => {
      if (auth) {
        api.setAuth(auth as AuthConfig);
      }
      const config: RequestConfig = {
        parameters: params || {},
      };
      if (body !== undefined) {
        config.requestBody = body;
      }
      return func(auth as AuthConfig, config);
    };
  }

  return {
    mapType: ExecutorType.RESTAPIHANDLER,
    map
  };
} 
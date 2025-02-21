import { Method } from 'axios';
import { RestApiHandler } from '../core/rest-api-handler';
import { AuthConfig } from '../types/auth';

/**
 * Matches URL path parameters in the format :paramName
 * Valid parameter names must start with a letter and can contain letters, numbers, and underscores
 */
const PATH_PARAM_REGEX = /:([a-zA-Z][a-zA-Z0-9_]*)/g;

export interface PathDefinition {
  path: string;
  method: Method;
  operationId: string;
}

/**
 * Extracts parameter names from a URL path string
 * Example: For path "/users/:id/posts/:postId"
 * PathParams<typeof path> = "id" | "postId"
 */
type PathParams<T extends string> = string extends T
  ? string
  : T extends `${string}:${infer Param}/${infer Rest}`
    ? Param | PathParams<Rest>
    : T extends `${string}:${infer Param}`
      ? Param
      : never;

/**
 * Creates a type-safe parameter object from a URL path
 * Example: For path "/users/:id/posts/:postId"
 * ExtractPathParams<typeof path> = { id: string; postId: string }
 */
type ExtractPathParams<T extends string> = {
  [K in PathParams<T>]: string;
};

export interface RequestConfig<P = Record<string, unknown>> {
  parameters?: P;
  requestBody?: Record<string, unknown>;
}

export type ApiFunction<P = Record<string, unknown>> = (
  auth: AuthConfig,
  config: RequestConfig<P>
) => Promise<Record<string, unknown>>;

export type ApiMap = Record<string, ApiFunction>;

/**
 * Creates an API map from path definitions
 * @param api RestApiHandler instance
 * @param paths Array of path definitions
 * @returns Generated API map
 * 
 * @example
 * const paths = [
 *   { path: '/tweets', method: 'POST', operationId: 'postTweet' },
 *   { path: '/tweets/:id', method: 'GET', operationId: 'getTweet' },
 * ];
 * 
 * const map = createApiMap(api, paths);
 * // Generates:
 * // {
 * //   postTweet: async (auth, { parameters, requestBody }) => {...},
 * //   getTweet: async (auth, { parameters }) => {...},
 * // }
 */
export function createApiMap(api: RestApiHandler, paths: readonly PathDefinition[]): ApiMap {
  return paths.reduce((acc, { path, method, operationId }) => {
    acc[operationId] = async (auth: AuthConfig, { parameters, requestBody }: RequestConfig) => {
      api.setAuth(auth);

      // Extract path parameters from the path definition
      const pathParamMatches = path.match(PATH_PARAM_REGEX) || [];
      const pathParams = pathParamMatches.reduce((params, match) => {
        const paramName = match.slice(1); // Remove the : prefix
        const paramValue = parameters?.[paramName];
        if (paramValue && typeof paramValue === 'string') {
          params[paramName] = paramValue;
        }
        return params;
      }, {} as Record<string, string>);

      // Remove path parameters from the parameters object
      const queryParams = { ...parameters };
      Object.keys(pathParams).forEach((key) => delete queryParams[key]);

      switch (method.toUpperCase()) {
        case 'GET':
          return api.get(path, queryParams, pathParams);
        case 'POST':
          return api.post(path, requestBody, queryParams, pathParams);
        case 'PUT':
          return api.put(path, requestBody, queryParams, pathParams);
        case 'PATCH':
          return api.patch(path, requestBody, queryParams, pathParams);
        case 'DELETE':
          return api.delete(path, queryParams, pathParams);
        default:
          throw new Error(`Unsupported HTTP method: ${method}`);
      }
    };
    return acc;
  }, {} as ApiMap);
} 
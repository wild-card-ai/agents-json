import { Bundle } from './models/bundle.js';
import { Flow, Link } from './models/schema.js';
import { AuthConfig, AuthType, OAuth1AuthConfig, OAuth2AuthConfig, UserPassCredentials } from './models/auth.js';
import { convertDotDigitsToBrackets, get, set, deepMerge } from './utils.js';

type ExecutionTrace = Record<string, {
  parameters: Record<string, any>;
  requestBody: Record<string, any>;
  responses: Record<string, any>;
}>;

interface ApplyLinkParams {
  link: Link;
  executionTrace: ExecutionTrace;
}

interface ResolveAuthParams {
  auth: AuthConfig;
}

interface ExecuteParams {
  bundle: Bundle;
  flow: Flow;
  auth: AuthConfig;
  parameters?: Record<string, any>;
  requestBody?: Record<string, any>;
  integrations?: Record<string, any>;
}

interface ExecuteFlowsParams {
  flows: Flow[];
  bundle: Bundle;
  auth: AuthConfig;
  parameters?: Record<string, any>;
  requestBody?: Record<string, any>;
}

/**
 * Maps values between actions using dot notation support,
 * including array indexing like line_items[0].quantity.
 */
export function applyLink({ link, executionTrace }: ApplyLinkParams): Record<string, Record<string, any>> {
  const apply = {
    parameters: {},
    requestBody: {},
    responses: {}
  };

  // Get the source value using the field path
  const sourceTrace = executionTrace[link.origin.actionId ?? ''];
  const fieldPath = convertDotDigitsToBrackets(link.origin.fieldPath);
  const sourceValue = get(sourceTrace, fieldPath);

  // If the source value does not exist, return empty result
  if (sourceValue === undefined) {
    return apply;
  }

  // Apply the value to the target field
  const targetPath = convertDotDigitsToBrackets(link.target.fieldPath);
  set(apply, targetPath, sourceValue);

  return apply;
}

/**
 * Resolve the auth configuration to the appropriate format
 */
export function resolveAuth({ auth }: ResolveAuthParams): string | [string, string] | OAuth1AuthConfig | OAuth2AuthConfig {
  switch (auth.type) {
    case AuthType.OAUTH1:
    case AuthType.OAUTH2:
      return auth;
    case AuthType.API_KEY:
      return auth.keyValue;
    case AuthType.BEARER:
      return auth.token;
    case AuthType.BASIC:
      const credentials = auth.credentials;
      if (typeof credentials === 'string') {
        return credentials;
      } else if (credentials && 'username' in credentials) {
        return [credentials.username, credentials.password];
      }
      throw new Error(`Unsupported auth credentials type: ${typeof credentials}`);
    default:
      throw new Error(`Unsupported auth type: ${auth}`);
  }
}

/**
 * Execute a flow of Actions in order, applying link-based parameter mapping.
 * Each new mapping is deep-merged to preserve nested structures.
 */
export async function execute({ bundle, flow, auth, parameters = {}, requestBody = {}, integrations = {} }: ExecuteParams): Promise<Record<string, any>> {
  if (!flow.actions.length) {
    return {};
  }

  // Initialize execution trace with flow parameters
  const executionTrace: ExecutionTrace = {
    [flow.id]: {
      parameters,
      requestBody,
      responses: {}
    }
  };

  // Execute each action in order
  for (const action of flow.actions) {
    try {
      // Get integration either from passed integrations or try dynamic import
      let integration;
      if (integrations[action.sourceId]) {
        integration = integrations[action.sourceId];
      }

      if (!integration) {
        throw new Error(`Integration ${action.sourceId} not found`);
      }

      const { operationType, operations } = integration;
      const operation = operations[action.operationId];

      if (!operation) {
        throw new Error(`Operation ${action.operationId} not found in integration ${action.sourceId}`);
      }

      // Initialize action trace
      executionTrace[action.id] = {
        parameters,
        requestBody: {},
        responses: {}
      };

      // Execute the operation
      const response = await operation({
        parameters,
        requestBody: {},
        auth: resolveAuth({ auth })
      });

      // Store the response
      executionTrace[action.id].responses = response;
    } catch (error) {
      console.error(`Error executing action ${action.id}:`, error);
      throw error;
    }
  }

  return executionTrace;
}

/**
 * Execute multiple flows in parallel
 */
export async function executeFlows({ flows, bundle, auth, parameters = {}, requestBody = {} }: ExecuteFlowsParams): Promise<Record<string, any>> {
  const results: Record<string, any> = {};

  await Promise.all(
    flows.map(async flow => {
      try {
        results[flow.id] = await execute({ bundle, flow, auth, parameters, requestBody });
      } catch (error) {
        if (error instanceof Error) {
          console.error(`Error executing flow ${flow.id}:`, error);
          results[flow.id] = { error: error.message };
        }
      }
    })
  );

  return results;
}

import _ from 'lodash';
import {
  AuthConfig,
  AuthType,
} from '../types/auth';
import {
  Bundle,
} from '../types/bundle';
import {
  ExecutorType,
} from '../types/tools';
import { Flow, Link, Origin, Target } from '../types/schema';
import {
  OpenAIResponse,
  AuthResult as AuthResultType,
  IntegrationModule,
  ExecutionTrace,
  ExecuteResult,
} from '../types/executor';

// Cache for initialized integrations
const integrationCache = new Map<string, Promise<IntegrationModule>>();

/**
 * Initialize an integration if not already initialized
 */
async function getIntegration(sourceId: string, bundle: Bundle, auth?: AuthConfig): Promise<IntegrationModule> {
  if (!integrationCache.has(sourceId)) {
    // Dynamically import and initialize the integration
    const integration = import(`../integrations/${sourceId}`);
    integrationCache.set(sourceId, integration.then(mod => mod.createIntegration(bundle, auth)));
  }
  return integrationCache.get(sourceId)!;
}

/**
 * Maps values between actions using lodash for robust dot notation support
 */
function applyLink(
  origin: Origin,
  target: Target,
  executionTrace: ExecutionTrace
): Record<string, Record<string, unknown>> {
  const apply: Record<string, Record<string, unknown>> = {
    parameters: {},
    requestBody: {},
    responses: {},
  };

  const sourceTrace = executionTrace[origin.actionId ?? ''];
  const sourceValue = _.get(sourceTrace, origin.fieldPath);

  if (sourceValue === undefined) {
    return apply;
  }

  _.set(apply, target.fieldPath, sourceValue);
  return apply;
}

/**
 * Resolves authentication configuration into the appropriate format
 */
function resolveAuth(auth: AuthConfig): AuthResultType {
  if (!auth || typeof auth !== 'object' || !('type' in auth)) {
    throw new Error('Invalid auth configuration');
  }

  let result: AuthResultType;
  switch (auth.type) {
    case AuthType.OAUTH1:
    case AuthType.OAUTH2:
    case AuthType.API_KEY:
      result = auth;
      break;
    case AuthType.BEARER:
      result = auth.token;
      break;
    case AuthType.BASIC:
      if (typeof auth.credentials === 'string') {
        result = auth.credentials;
      } else {
        result = [auth.credentials.username, auth.credentials.password];
      }
      break;
    default:
      throw new Error(`Unsupported auth type: ${(auth as { type: string }).type}`);
  }
  return result;
}

/**
 * Executes a flow of Actions in order, applying link-based parameter mapping
 */
export async function execute(
  bundle: Bundle,
  flow: Flow,
  auth: AuthConfig,
  parameters: Record<string, unknown>,
  requestBody: Record<string, unknown>
): Promise<ExecuteResult> {
  if (!flow.actions?.length) {
    return {};
  }

  const executionTrace: ExecutionTrace = {
    [flow.id]: {
      parameters,
      requestBody,
      responses: {},
    },
  };

  for (const action of flow.actions) {
    try {
      // Get the operation from the bundle
      const operation = (bundle.operations as Record<string, unknown>)[action.operationId];
      if (!operation) {
        throw new Error(`Operation ${action.operationId} not found in bundle`);
      }

      // Find all links targeting this action
      const actionLinks = flow.links?.filter(
        (link: Link) => link.target.actionId === action.id
      ) ?? [];

      // Initialize action parameters
      let actionParameters: Record<string, unknown> = {};
      let actionRequestBody: Record<string, unknown> = {};

      // Apply each link and merge the results
      actionLinks.forEach((link: Link) => {
        const apply = applyLink(link.origin, link.target, executionTrace);
        actionParameters = _.merge(actionParameters, apply.parameters);
        actionRequestBody = _.merge(actionRequestBody, apply.requestBody);
      });

      // Store the parameters in execution trace
      executionTrace[action.id] = {
        parameters: actionParameters,
        requestBody: actionRequestBody,
      };

      // Get or initialize the integration
      const integration = await getIntegration(action.sourceId, bundle, auth);
      const operationFunc = integration.map[action.operationId];

      if (!operationFunc) {
        throw new Error(`Operation ${action.operationId} not found in integration ${action.sourceId}`);
      }

      // Execute the operation
      let result;
      if (integration.mapType === ExecutorType.RESTAPIHANDLER) {
        result = await operationFunc(resolveAuth(auth), actionParameters, actionRequestBody);
      } else {
        result = await operationFunc(resolveAuth(auth), { ...actionParameters, ...actionRequestBody });
      }

      if (!executionTrace[action.id].responses) {
        executionTrace[action.id].responses = {};
      }
      executionTrace[action.id].responses!.success = result;
    } catch (error) {
      console.error(`Error executing action ${action.id}:`, error);
      throw error;
    }
  }

  // Process flow response links
  const flowResponseLinks = flow.links?.filter(
    (link: Link) => link.target.actionId === flow.id && link.target.fieldPath.startsWith('responses')
  ) ?? [];

  if (!flowResponseLinks.length) {
    // If no response links defined, return the last action's response
    const lastAction = flow.actions[flow.actions.length - 1];
    return executionTrace[lastAction.id]?.responses ?? {};
  }

  // Merge all flow response links
  let flowResponses = executionTrace[flow.id]?.responses ?? {};
  for (const link of flowResponseLinks) {
    const apply = applyLink(link.origin, link.target, executionTrace);
    if (apply.responses) {
      flowResponses = _.merge(flowResponses, apply.responses);
    }
  }

  return flowResponses;
}

/**
 * Wrapper around `execute` that parses a tool call response to execute the flows
 */
export async function executeFlows(
  response: OpenAIResponse,
  bundle: Bundle,
  flows: Flow[],
  auth: AuthConfig
): Promise<Record<string, ExecuteResult>> {
  const results: Record<string, ExecuteResult> = {};

  if (!response.choices?.[0]?.message?.tool_calls) {
    return { message: (response.choices?.[0]?.message?.content ?? '') as unknown as ExecuteResult };
  }

  for (const toolCall of response.choices[0].message.tool_calls) {
    const argsDict = JSON.parse(toolCall.function.arguments);
    const flow = flows.find((f) => f.id === toolCall.function.name);

    if (!flow) {
      throw new Error(`Flow ${toolCall.function.name} not found`);
    }

    let parameters: Record<string, unknown> = {};
    let requestBody: Record<string, unknown> = {};

    if (!('parameters' in argsDict) && !('requestBody' in argsDict)) {
      requestBody = argsDict;  // If no explicit parameters/requestBody, treat all args as requestBody
    } else {
      parameters = argsDict.parameters ?? {};
      requestBody = argsDict.requestBody ?? {};
    }

    results[flow.id] = await execute(bundle, flow, auth, parameters, requestBody);
  }

  return results;
} 
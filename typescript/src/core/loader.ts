import _ from 'lodash';
import { AgentsJsonSchema, Override, Source } from '../types/schema';
import { Bundle } from '../types/bundle';

/**
 * Apply a list of overrides to an OpenAPI source document
 */
export function applyOverrides(openApiSource: Record<string, unknown>, overrides: Override[]): Record<string, unknown> {
  const result = { ...openApiSource };
  
  for (const override of overrides) {
    if (override.fieldPath && override.value !== undefined) {
      _.set(result, override.fieldPath, override.value);
    }
  }
  
  return result;
}

/**
 * Load an OpenAPI source document from a URL
 */
export async function loadOpenApiSource(source: Source): Promise<Record<string, unknown>> {
  const response = await fetch(source.path);
  if (!response.ok) {
    throw new Error(`Failed to fetch OpenAPI spec from ${source.path}: ${response.status}`);
  }

  const contentType = response.headers.get('content-type');
  let parsedData: Record<string, unknown>;

  if (source.path.toLowerCase().endsWith('.yaml') || source.path.toLowerCase().endsWith('.yml') || contentType?.includes('yaml')) {
    // For YAML files, we'll need to use a YAML parser
    const yaml = await import('js-yaml');
    const text = await response.text();
    parsedData = yaml.load(text) as Record<string, unknown>;
  } else {
    parsedData = await response.json();
  }

  return parsedData;
}

/**
 * Creates a dictionary mapping operationIds to their operation info from an OpenAPI spec
 */
export function indexByOperationId(spec: Record<string, unknown>): Record<string, unknown> {
  const httpMethods = ['get', 'post', 'put', 'delete', 'patch', 'options', 'head'];
  const paths = spec.paths as Record<string, Record<string, unknown>> || {};
  const operations: Record<string, unknown> = {};

  for (const [path, pathItem] of Object.entries(paths)) {
    for (const method of httpMethods) {
      const operation = pathItem[method] as Record<string, unknown> | undefined;
      if (operation && operation.operationId) {
        operations[operation.operationId as string] = {
          ...operation,
          path,
          method,
        };
      }
    }
  }

  return operations;
}

/**
 * Extract the base URL from an OpenAPI spec
 */
function extractBaseUrl(spec: Record<string, unknown>): string {
  // Try OpenAPI 3.0 servers array first
  const servers = spec.servers as Array<{ url: string }> | undefined;
  if (servers && servers.length > 0) {
    return servers[0].url;
  }

  // Fallback to OpenAPI 2.0 (Swagger) host + basePath
  const host = spec.host as string | undefined;
  const basePath = spec.basePath as string | undefined;
  const schemes = spec.schemes as string[] | undefined;
  
  if (host) {
    const scheme = schemes && schemes.length > 0 ? schemes[0] : 'https';
    return `${scheme}://${host}${basePath || ''}`;
  }

  throw new Error('Could not extract base URL from OpenAPI spec');
}

/**
 * Load and parse an agents.json file
 */
export async function loadAgentsJson(url: string): Promise<Bundle> {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Failed to fetch agents.json from ${url}: ${response.status}`);
  }

  const content = await response.json();
  const agentsJson = AgentsJsonSchema.parse(content);
  
  // Get the first source - in the future we might want to support multiple sources
  if (!agentsJson.sources || agentsJson.sources.length === 0) {
    throw new Error('No sources defined in agents.json');
  }
  const source = agentsJson.sources[0];

  const openApiSource = await loadOpenApiSource(source);
  const openapi = applyOverrides(openApiSource, agentsJson.overrides || []);
  const operations = indexByOperationId(openapi);
  const baseURL = extractBaseUrl(openapi);

  return {
    agentsJson,
    openapi,
    operations,
    baseURL
  };
} 
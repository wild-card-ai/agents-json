import { AgentsJsonSchema, Override, Source } from '../models/schema';
import { Bundle } from './models/bundle';
import { convertDotDigitsToBrackets } from './utils';
import yaml from 'js-yaml';

interface ApplyOverridesParams {
  openApiSource: Record<string, any>;
  overrides: Override[];
}

interface LoadOpenApiSourceParams {
  source: Source;
}

interface IndexByOperationIdParams {
  spec: Record<string, any>;
}

interface LoadAgentsJsonParams {
  url: string;
}

/**
 * Apply a list of overrides to an OpenAPI source document
 */
export function applyOverrides({ openApiSource, overrides }: ApplyOverridesParams): Record<string, any> {
  const result = { ...openApiSource };

  for (const override of overrides) {
    if (override.fieldPath && override.value !== undefined) {
      const fieldPath = convertDotDigitsToBrackets(override.fieldPath);
      let current = result;
      const keys = fieldPath.split(/[.[\]]+/).filter(Boolean);

      for (let i = 0; i < keys.length - 1; i++) {
        const key = keys[i];
        if (!(key in current)) {
          current[key] = /^\d+$/.test(keys[i + 1]) ? [] : {};
        }
        current = current[key];
      }

      const lastKey = keys[keys.length - 1];
      current[lastKey] = override.value;
    }
  }

  return result;
}

/**
 * Load an OpenAPI source document from a URL or local file
 */
export async function loadOpenApiSource({ source }: LoadOpenApiSourceParams): Promise<Record<string, any>> {
  let content: string;

  console.log(source)

  // Handle local file paths
  if (source.path.startsWith('/') || source.path.startsWith('./')) {
    const fs = await import('fs/promises');
    content = await fs.readFile(source.path, 'utf-8');
  } else {
    // Handle HTTP/HTTPS URLs
    const response = await fetch(source.path);
    if (!response.ok) {
      throw new Error(`Failed to fetch OpenAPI spec from ${source.path}: ${response.status}`);
    }
    content = await response.text();
    console.log(content, 'yo!')
  }

  if (!content.trim()) {
    throw new Error('Empty response received');
  }

  // Parse YAML or JSON
  try {
    if (source.path.endsWith('.yaml') || source.path.endsWith('.yml')) {
      return yaml.load(content) as Record<string, any>;
    } else {
      return JSON.parse(content);
    }
  } catch (error) {
    throw new Error(`Failed to parse OpenAPI spec: ${error}`);
  }
}

/**
 * Creates a dictionary mapping operationIds to their operation info from an OpenAPI spec
 */
export function indexByOperationId({ spec }: IndexByOperationIdParams): Record<string, any> {
  const HTTP_METHODS = ['get', 'post', 'put', 'delete', 'patch', 'options', 'head'];
  const result: Record<string, any> = {};

  const paths = spec.paths || {};
  for (const [path, pathItem] of Object.entries(paths)) {
    for (const method of HTTP_METHODS) {
      const operation = (pathItem as any)[method];
      if (operation && operation.operationId) {
        result[operation.operationId] = {
          ...operation,
          path,
          method
        };
      }
    }
  }

  return result;
}

/**
 * Loads an agents.json file and returns a Bundle containing the parsed agents.json,
 * the OpenAPI spec, and the indexed operations
 */
export async function loadAgentsJson({ url }: LoadAgentsJsonParams): Promise<Bundle> {
  let content: string;

  // Handle local file paths
  if (url.startsWith('/') || url.startsWith('./')) {
    const fs = await import('fs/promises');
    content = await fs.readFile(url, 'utf-8');
  } else {
    // Handle HTTP/HTTPS URLs
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Failed to fetch agents.json from ${url}: ${response.status}`);
    }
    content = await response.text();
  }

  if (!content.trim()) {
    throw new Error('Empty response received');
  }

  const data = JSON.parse(content);
  const agentsJson = AgentsJsonSchema.parse(data);

  // Get the first source (maintaining Python behavior)
  const source = agentsJson.sources[0];
  if (!source) {
    throw new Error('No sources defined in agents.json');
  }

  // Load and process OpenAPI spec
  const openApiSource = await loadOpenApiSource({ source });
  const modifiedSpec = applyOverrides({ openApiSource, overrides: agentsJson.overrides || [] });
  const indexedSpec = indexByOperationId({ spec: modifiedSpec });

  return {
    agentsJson,
    openapi: modifiedSpec,
    operations: indexedSpec
  };
}

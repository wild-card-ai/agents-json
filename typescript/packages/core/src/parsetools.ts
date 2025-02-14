import { z } from 'zod';
import { Flow } from './models/schema.js';
import { createTool } from '@mastra/core';

function parameterToZodSchema(param: any): z.ZodType<any> {
  let schema: z.ZodType<any>;

  // Convert parameter type to Zod schema
  switch (param.type?.toLowerCase()) {
    case 'number':
      schema = z.number();
      break;
    case 'boolean':
      schema = z.boolean();
      break;
    case 'array':
      schema = z.array(z.any()); // Could be more specific if we had item type
      break;
    case 'object':
      schema = z.record(z.any()); // Could be more specific if we had property types
      break;
    default:
      schema = z.string();
  }

  // Add description if available
  if (param.description) {
    schema = schema.describe(param.description);
  }

  // Make optional if not required
  if (!param.required) {
    schema = schema.optional();
  }

  return schema;
}

export function toMastra(flow: Flow, map: any, apiKey: string): any {
  let inputSchema: z.ZodObject<any> = z.object({});

  // Create schema parts
  const schemaParts: Record<string, z.ZodType> = {};

  // Add parameters to schema if they exist
  if (flow.fields.parameters.length > 0) {
    const paramSchema = flow.fields.parameters.reduce(
      (acc, param) => ({
        ...acc,
        [param.name]: parameterToZodSchema(param)
      }),
      {}
    );
    schemaParts.parameters = z.object(paramSchema);
  } else {
    schemaParts.parameters = z.object({});
  }

  // Add request body to schema if it exists
  if (flow.fields.requestBody?.content) {
    const contentType = 'application/json' in flow.fields.requestBody.content
      ? 'application/json'
      : Object.keys(flow.fields.requestBody.content)[0];

    const content = flow.fields.requestBody.content[contentType];
    if (content.schema) {
      schemaParts.requestBody = parameterToZodSchema(content.schema);
    }
  }

  // Combine into final schema
  inputSchema = z.object(schemaParts);

  return createTool({
    id: flow.id,
    description: flow.description,
    inputSchema,
    execute: async ({ context }) => {
      const executeFn = map[flow.actions[0].operationId];
      if (!executeFn) {
        throw new Error(`No implementation found for operation: ${flow.actions[0].operationId}`);
      }
      return executeFn(apiKey, context.parameters || {});
    }
  });
}
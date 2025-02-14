import { z } from 'zod';
import { createTool } from '@mastra/core';
import type { Tool } from '@mastra/core';

export enum IntegrationType {
  SDK = 'sdk',
  REST = 'rest',
  CUSTOM = 'custom'
}

export const IntegrationMethodSchema = z.object({
  name: z.string(),
  description: z.string(),
  type: z.nativeEnum(IntegrationType),
  parameters: z.array(z.object({
    name: z.string(),
    type: z.string(),
    description: z.string().optional(),
    required: z.boolean().default(false)
  })),
  execute: z.function()
    .args(z.record(z.any()), // auth config
      z.record(z.any())) // parameters))
    .returns(z.promise(z.any()))
});

export type IntegrationMethod = z.infer<typeof IntegrationMethodSchema>;

export const IntegrationSchema = z.object({
  id: z.string(),
  type: z.nativeEnum(IntegrationType),
  methods: z.record(z.string(), IntegrationMethodSchema)
});

export type Integration = z.infer<typeof IntegrationSchema>;

// Registry to manage all integrations
export class IntegrationRegistry {
  private integrations: Map<string, Integration> = new Map();

  register(integration: Integration): void {
    if (this.integrations.has(integration.id)) {
      throw new Error(`Integration with id ${integration.id} already exists`);
    }
    this.integrations.set(integration.id, integration);
  }

  get(id: string): Integration | undefined {
    return this.integrations.get(id);
  }

  getMethod(integrationId: string, methodName: string): IntegrationMethod | undefined {
    const integration = this.integrations.get(integrationId);
    return integration?.methods[methodName];
  }

  list(): Integration[] {
    return Array.from(this.integrations.values());
  }

  // Get all methods in a format suitable for AI tools
  toTools() {
    return this.list().flatMap(integration =>
      Object.entries(integration.methods).map(([name, method]) => {
        // Create Zod schema for parameters
        const parameterProperties: Record<string, z.ZodTypeAny> = {};
        method.parameters.forEach(param => {
          let paramSchema = z.string(); // Default to string
          if (param.type === 'number') paramSchema = z.number();
          if (param.type === 'boolean') paramSchema = z.boolean();

          paramSchema = param.required ? paramSchema : paramSchema.optional();
          parameterProperties[param.name] = paramSchema;
        });

        return {
          name: `${integration.id}_${name}`,
          description: method.description,
          parameters: z.object(parameterProperties),
          execute: async (auth: Record<string, any>, params: Record<string, any>) => {
            return this.execute(integration.id, name, auth, params);
          }
        };
      })
    );
  }

  // Get all methods as a map of tools
  getTools(): Map<string, {
    name: string;
    description: string;
    parameters: z.ZodObject<any>;
    execute: (auth: Record<string, any>, params: Record<string, any>) => Promise<any>
  }> {
    const toolMap = new Map();

    this.list().forEach(integration => {
      Object.entries(integration.methods).forEach(([methodName, method]) => {
        const toolName = `${integration.id}_${methodName}`;

        // Create Zod schema for parameters
        const parameterProperties: Record<string, z.ZodTypeAny> = {};
        method.parameters.forEach(param => {
          let paramSchema = z.string(); // Default to string
          if (param.type === 'number') paramSchema = z.number();
          if (param.type === 'boolean') paramSchema = z.boolean();

          paramSchema = param.required ? paramSchema : paramSchema.optional();
          parameterProperties[param.name] = paramSchema;
        });

        toolMap.set(toolName, {
          name: toolName,
          description: method.description,
          parameters: z.object(parameterProperties),
          execute: method.execute
        });
      });
    });

    return toolMap;
  }

  // Execute a specific method
  async execute(integrationId: string, methodName: string, auth: Record<string, any>, params: Record<string, any>): Promise<any> {
    const method = this.getMethod(integrationId, methodName);
    if (!method) {
      throw new Error(`Method ${methodName} not found in integration ${integrationId}`);
    }
    return method.execute(auth, params);
  }

  // Convert registry tools to Mastra tools
  toMastraTools(authConfig: Record<string, any>): Record<string, Tool> {
    const tools = this.toTools();
    return Object.fromEntries(
      tools.map(tool => {
        const mastraTool = createTool({
          id: tool.name,
          inputSchema: tool.parameters as z.ZodObject<any>,
          description: tool.description,
          execute: async ({ context }) => {
            return tool.execute(authConfig, context);
          }
        });
        return [tool.name, mastraTool];
      })
    );
  }
}

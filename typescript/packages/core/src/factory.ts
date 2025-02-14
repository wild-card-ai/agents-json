import { z } from 'zod';
import { createTool, type Tool } from '@mastra/core/tools';
import { Integration, IntegrationSchema } from './types';

export function createIntegration(config: z.infer<typeof IntegrationSchema>): Integration {
  // Validate the config
  IntegrationSchema.parse(config);

  return {
    ...config,
    toTools() {
      return Object.entries(this.methods).map(([name, method]) => {
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
          name: `${this.id}_${name}`,
          description: method.description,
          parameters: z.object(parameterProperties),
          execute: method.execute
        };
      });
    },

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
  };
}

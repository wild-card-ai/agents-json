import { z } from 'zod';

// Schema for tool parameter
export const ToolParameterSchema = z.object({
  name: z.string().describe('Name of the parameter'),
  type: z.string().describe('Type of the parameter (e.g., string, number, boolean, object)'),
  description: z.string().optional().describe('Description of what the parameter does'),
  required: z.boolean().default(false).describe('Whether the parameter is required'),
  properties: z.record(z.any()).optional().describe('For object types, defines the nested properties'),
  items: z.any().optional().describe('For array types, defines the item structure')
});

export type ToolParameter = z.infer<typeof ToolParameterSchema>;

// Schema for tool definition
export const ToolSchema = z.object({
  name: z.string().describe('Name of the tool'),
  description: z.string().describe('Description of what the tool does'),
  parameters: z.array(ToolParameterSchema).describe('Parameters the tool accepts'),
  execute: z.function()
    .args(z.record(z.any()))
    .returns(z.promise(z.any()))
    .describe('Function to execute the tool with given parameters')
});

export type Tool = z.infer<typeof ToolSchema>;

// Helper function to convert our tool to Vercel AI SDK format
export function toVercelTool(tool: Tool) {
  return {
    name: tool.name,
    description: tool.description,
    parameters: {
      type: 'object',
      properties: tool.parameters.reduce((acc, param) => ({
        ...acc,
        [param.name]: {
          type: param.type,
          description: param.description
        }
      }), {}),
      required: tool.parameters
        .filter(param => param.required)
        .map(param => param.name)
    }
  };
}

// Tool registry to manage all available tools
export class ToolRegistry {
  private tools: Map<string, Tool> = new Map();

  register(tool: Tool): void {
    if (this.tools.has(tool.name)) {
      throw new Error(`Tool with name ${tool.name} already exists`);
    }
    this.tools.set(tool.name, tool);
  }

  get(name: string): Tool | undefined {
    return this.tools.get(name);
  }

  list(): Tool[] {
    return Array.from(this.tools.values());
  }

  // Get tools in a format suitable for AI tools integration
  getToolDefinitions() {
    return this.list().map(tool => ({
      name: tool.name,
      description: tool.description,
      parameters: {
        type: 'object',
        properties: tool.parameters.reduce((acc, param) => ({
          ...acc,
          [param.name]: {
            type: param.type,
            description: param.description
          }
        }), {}),
        required: tool.parameters
          .filter(param => param.required)
          .map(param => param.name)
      }
    }));
  }

  // Execute a specific tool
  async execute(name: string, params: Record<string, any>): Promise<any> {
    const tool = this.tools.get(name);
    if (!tool) {
      throw new Error(`Tool ${name} not found`);
    }
    return tool.execute(params);
  }
}

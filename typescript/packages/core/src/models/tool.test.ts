import { describe, it, expect } from 'vitest';
import { Tool, ToolRegistry } from './tool';

describe('ToolRegistry', () => {
  it('should manage tools and provide them in AI-compatible format', async () => {
    const registry = new ToolRegistry();

    // Define a sample tool
    const getPetTool: Tool = {
      name: 'getPetById',
      description: 'Get a pet from the store by its ID',
      parameters: [
        {
          name: 'id',
          type: 'integer',
          description: 'The ID of the pet to retrieve',
          required: true
        }
      ],
      execute: async (params: Record<string, any>) => {
        const { id } = params;
        return {
          id,
          name: 'Test Pet',
          type: 'dog'
        };
      }
    };

    // Register the tool
    registry.register(getPetTool);

    // Test tool listing
    expect(registry.list()).toHaveLength(1);
    expect(registry.list()[0].name).toBe('getPetById');

    // Test getting tool definitions
    const toolDefs = registry.getToolDefinitions();
    expect(toolDefs).toEqual([{
      name: 'getPetById',
      description: 'Get a pet from the store by its ID',
      parameters: {
        type: 'object',
        properties: {
          id: {
            type: 'integer',
            description: 'The ID of the pet to retrieve'
          }
        },
        required: ['id']
      }
    }]);

    // Test tool execution
    const result = await registry.execute('getPetById', { id: 123 });
    expect(result).toEqual({
      id: 123,
      name: 'Test Pet',
      type: 'dog'
    });
  });

  it('should prevent duplicate tool registration', () => {
    const registry = new ToolRegistry();
    const tool: Tool = {
      name: 'test',
      description: 'test tool',
      parameters: [],
      execute: async () => ({})
    };

    registry.register(tool);
    expect(() => registry.register(tool)).toThrow('Tool with name test already exists');
  });

  it('should throw error when executing non-existent tool', async () => {
    const registry = new ToolRegistry();
    await expect(registry.execute('nonexistent', {}))
      .rejects
      .toThrow('Tool nonexistent not found');
  });
});

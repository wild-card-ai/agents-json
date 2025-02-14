import { describe, it, expect } from 'vitest';
import { execute } from './executor';
import { Bundle } from './models/bundle';
import { Flow } from '../models/schema';
import { AuthType } from './models/auth';

describe('Executor', () => {
  it('should execute a simple API call with API key auth', async () => {
    // Mock OpenAPI spec for a simple pet store API
    const openApiSpec = {
      openapi: '3.0.0',
      info: {
        title: 'Pet Store API',
        version: '1.0.0'
      },
      paths: {
        '/pets/{id}': {
          get: {
            operationId: 'getPetById',
            parameters: [
              {
                name: 'id',
                in: 'path',
                required: true,
                schema: {
                  type: 'integer'
                }
              }
            ],
            responses: {
              '200': {
                description: 'Pet found',
                content: {
                  'application/json': {
                    schema: {
                      type: 'object',
                      properties: {
                        id: { type: 'integer' },
                        name: { type: 'string' },
                        type: { type: 'string' }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    };

    // Create a bundle with the OpenAPI spec
    const bundle: Bundle = {
      agentsJson: {
        agentsJson: '1.0.0',
        info: {
          title: 'Test API',
          version: '1.0.0',
          description: 'Test API for executor tests'
        },
        sources: [],
        flows: []
      },
      openapi: openApiSpec,
      operations: {
        getPetById: {
          operationId: 'getPetById',
          parameters: [
            {
              name: 'id',
              in: 'path',
              required: true,
              schema: { type: 'string' }
            }
          ]
        }
      }
    };

    // Define a simple flow that gets a pet by ID
    const flow: Flow = {
      id: 'get_pet',
      title: 'Get Pet by ID',
      description: 'Retrieves a pet from the petstore by its ID',
      actions: [
        {
          id: 'get_pet_action',
          sourceId: 'petstore',
          operationId: 'getPetById'
        }
      ],
      fields: {
        parameters: [
          {
            name: 'id',
            type: 'integer',
            required: true
          }
        ],
        responses: {
          success: {
            type: 'object',
            description: 'Pet object'
          }
        }
      }
    };

    // Define API key auth
    const auth = {
      type: AuthType.API_KEY,
      keyValue: 'test-api-key'
    } as const;

    // Mock integrations
    const mockIntegrations = {
      petstore: {
        operationType: 'rest',
        operations: {
          getPetById: async ({ parameters }) => ({
            id: parameters.id,
            name: 'Test Pet',
            type: 'dog'
          })
        }
      }
    };

    // Execute the flow
    const result = await execute({
      bundle,
      flow,
      auth,
      parameters: { id: 123 },
      requestBody: {},
      integrations: mockIntegrations
    });

    // Verify the result structure
    expect(result).toBeDefined();
    expect(result.get_pet_action).toBeDefined();
    expect(result.get_pet_action.parameters).toEqual({
      id: 123
    });
    expect(result.get_pet_action.responses).toEqual({
      id: 123,
      name: 'Test Pet',
      type: 'dog'
    });
  });
});

// Translated from Python parsetools.py to TypeScript

import { Flow, Parameter } from '../types/schema';
import { ToolFormat } from '../types/tools';

/**
 * Converts a list of Flow objects into tools based on the specified format.
 * @param flows - The list of Flow objects to convert.
 * @param format - The format to convert the flows into.
 * @returns An array of tools in the specified format.
 * @throws Will throw an error if the tool format is unsupported.
 */
export function flowsTools(flows: Flow[], format: ToolFormat): Record<string, any>[] {
  if (format === ToolFormat.OPENAI) {
    return flows.map(flow => flowToOpenaiTool(flow));
  } else if (format === ToolFormat.JSON) {
    return flows.map(flow => flowToJsonTool(flow));
  } else {
    throw new Error(`Unsupported tool format: ${format}`);
  }
}

/**
 * Generates a slim representation of flows to add to an LLM system prompt.
 * @param flows - The list of Flow objects.
 * @returns A string representation of the flows.
 */
export function flowsPrompt(flows: Flow[]): string {
  return flows.map(flow => `${flow.id}: ${flow.description}`).join("\n");
}

/**
 * Converts a Flow object to an OpenAI function-calling tool format.
 * @param flow - The Flow object to convert.
 * @returns A tool object compatible with OpenAI's function-calling format.
 */
function flowToOpenaiTool(flow: Flow): Record<string, any> {
  /**
   * Helper function to convert JSON schema to OpenAI format recursively.
   * @param schema - The JSON schema to convert.
   * @returns The converted OpenAI-compatible schema.
   */
  function convertSchemaToOpenai(schema: Record<string, any>): Record<string, any> {
    if ("anyOf" in schema) {
      return {
        anyOf: schema["anyOf"].map((option: Record<string, any>) => convertSchemaToOpenai(option))
      };
    } else if (schema.type === "object" && schema.properties) {
      const properties: Record<string, any> = {};
      for (const [propName, propSchema] of Object.entries(schema.properties)) {
        properties[propName] = convertSchemaToOpenai(propSchema as Record<string, any>);
      }
      const result: Record<string, any> = {
        type: "object",
        properties
      };
      if (schema.required) {
        result.required = schema.required;
      }
      return result;
    } else if (schema.type === "array" && schema.items) {
      return {
        type: "array",
        items: convertSchemaToOpenai(schema.items as Record<string, any>)
      };
    } else {
      const result: Record<string, any> = {
        type: schema.type || "string",
        description: schema.description || ""
      };
      if (schema.enum) {
        result.enum = schema.enum;
      }
      if (schema.format) {
        result.format = schema.format;
      }
      return result;
    }
  }

  const properties: Record<string, any> = {};

  // Handle parameters
  if (flow.fields.parameters && flow.fields.parameters.length > 0) {
    const paramsProperties: Record<string, any> = {};
    const requiredParams: string[] = [];

    flow.fields.parameters.forEach((param: Parameter) => {
      paramsProperties[param.name] = {
        type: param.type || "string", // Default to string if type is not provided
        description: param.description || ""
      };
      if (param.required) {
        requiredParams.push(param.name);
      }
    });

    properties["parameters"] = {
      type: "object",
      properties: paramsProperties,
      required: requiredParams
    };
  }

  // Handle request body
  if (flow.fields.requestBody && flow.fields.requestBody.content) {
    const contentTypes = Object.keys(flow.fields.requestBody.content);
    const contentType = contentTypes.includes("application/json") 
      ? "application/json" 
      : contentTypes[0];

    const content = flow.fields.requestBody.content[contentType];
    if (content.schema) {
      const convertedRequestBody = convertSchemaToOpenai(content.schema);
      properties["requestBody"] = convertedRequestBody;
    }
  }

  return {
    type: "function",
    function: {
      name: flow.id,
      description: flow.description,
      parameters: {
        type: "object",
        properties: properties,
        required: Object.keys(properties)
      },
      additionalProperties: false
    }
  };
}

/**
 * Converts a Flow object to a JSON tool format.
 * @param flow - The Flow object to convert.
 * @returns A tool object in JSON format.
 */
function flowToJsonTool(flow: Flow): Record<string, any> {
  return {
    type: "function",
    function: {
      name: flow.id,
      description: flow.description,
      parameters: {
        parameters: flow.fields.parameters,
        requestBody: flow.fields.requestBody,
        responses: flow.fields.responses
      }
    }
  };
}
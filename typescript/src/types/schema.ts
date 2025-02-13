// Translated from Python Pydantic models to TypeScript Zod schemas

import { z } from 'zod';

// Info Schema
export const InfoSchema = z.object({
  title: z.string().describe('MUST provide the title of the `agents.json` specification. This title serves as a human-readable name for the specification.'),
  version: z.string().describe('MUST follow the Semantic Versioning (SemVer) format as defined in https://semver.org/. This version identifier ensures strict version control and compatibility management.'),
  description: z.string().describe('MUST include a comprehensive description of the `agents.json` specification. This description should outline its purpose, functionality, and key features, facilitating understanding and implementation by users and Large Language Models (LLMs).'),
}).passthrough();

// Source Schema
export const SourceSchema = z.object({
  id: z.string().describe('MUST provide a unique, human-readable identifier for the API source. Identifiers MUST be in snake_case format and globally unique within the `agents.json` context, ensuring clear reference and invocation. **Example**: `user_service`'),
  path: z.string().describe('MUST specify the file path or URL to the OpenAPI 3+ specification of the API source. The path SHOULD follow a structured format using dot notation and array indices where necessary (e.g., `components.schemas.User`).'),
}).passthrough();

// Override Schema
export const OverrideSchema = z.object({
  sourceId: z.string().describe('MUST correspond to an `id` in the `sources` array. This ensures the override targets a valid API source.'),
  operationId: z.string().describe('MUST match an `operationId` in the referenced OpenAPI specification. This ensures accurate targeting of the operation to be overridden.'),
  fieldPath: z.string().describe('MUST be a JSON path expression that specifies the exact field within the operation to modify. The path SHOULD traverse the OpenAPI operation hierarchy using dot notation and array indices (e.g., `parameters.0.required`), treating the OpenAPI operation as the root.'),
  value: z.union([
    z.string(),
    z.record(z.unknown()),
    z.array(z.unknown()),
    z.boolean(),
    z.number(),
  ]).describe('MUST assign a new value to the specified field. Supports multiple data types to allow for flexible and comprehensive overrides of operation fields.'),
}).passthrough();

// Action Schema
export const ActionSchema = z.object({
  id: z.string().describe('MUST provide a unique, human-readable identifier for the action within the flow. Identifiers MUST be in snake_case format and unique within the flow, enabling precise reference in links. **Example**: `validate_payment`'),
  sourceId: z.string().describe('MUST reference the `id` of an API source defined in the `sources` array. Indicates which API the action is associated with, ensuring correct operation execution.'),
  operationId: z.string().describe('MUST identify the specific operation within the API source to execute. Must match an `operationId` in the referenced OpenAPI specification, ensuring accurate and intended operation invocation.'),
}).passthrough();

// Origin Schema
export const OriginSchema = z.object({
  actionId: z.string().optional().describe("OPTIONAL. The identifier of the action providing the data. If null, the source is the flow's input parameters."),
  fieldPath: z.string().describe('MUST be a JSON path expression specifying the source field from which to extract data. The path SHOULD traverse the OpenAPI operation hierarchy using dot notation and array indices (e.g., `response.data.items.0.name`), treating the OpenAPI operation as the root.'),
}).passthrough();

// Target Schema
export const TargetSchema = z.object({
  actionId: z.string().optional().describe("OPTIONAL. The identifier of the action receiving the data. If null, the target is the flow's response fields, allowing data to be outputted to the user."),
  fieldPath: z.string().describe('MUST be a JSON path expression specifying the destination field where the data should be placed. The path SHOULD traverse the OpenAPI operation hierarchy using dot notation and array indices (e.g., `parameters.userId`), treating the OpenAPI operation as the root.'),
}).passthrough();

// Link Schema
export const LinkSchema = z.object({
  origin: OriginSchema.describe("MUST specify the data origin for the link, which can be an action's response or the flow's input parameters."),
  target: TargetSchema.describe("MUST specify the destination location for the mapped data, targeting an action's parameters or the flow's response fields."),
}).strict();

// Parameter Schema
export const ParameterSchema = z.object({
  name: z.string().describe('MUST provide the name of the parameter. This name is used to reference the parameter in links and user interactions, ensuring consistency and clarity.'),
  description: z.string().optional().describe('OPTIONAL. A detailed description of the parameter, explaining its purpose, usage, and any constraints. This aids users in understanding what is expected when providing input.'),
  required: z.boolean().optional().default(false).describe('OPTIONAL. Indicates whether the parameter is mandatory (`true`) or optional (`false`) when invoking the flow.'),
  type: z.string().optional().describe('The type of the parameter. This can be a primitive type (e.g., `string`, `number`, `boolean`, `array`, `object`) or a complex type (e.g., `array`, `object`). If not provided, the type is inferred from the context.'),
}).strict();

// Content Schema
export const ContentSchema = z.object({
  schema: z.record(z.any()).describe('MUST provide the schema defining the structure of the request body for the specified MIME type. Follows JSON Schema specifications as per RFC 7159, enabling precise data validation and formatting.'),
  example: z.record(z.any()).optional().describe('OPTIONAL. An example of the request body content for the specified MIME type. Provides practical illustrations of expected data formats and structures.'),
}).strict();

// RequestBody Schema
export const RequestBodySchema = z.object({
  content: z.record(ContentSchema).optional().describe('MUST include a map of MIME types to their corresponding schemas defining the request body. Each key MUST conform to the media type format as per RFC 7231, enabling content negotiation and proper data handling.'),
  required: z.boolean().optional().default(false).describe('OPTIONAL. Specifies whether the request body is required (`true`) or optional (`false`) for the flow.'),
}).strict();

// Responses Schema
export const ResponsesSchema = z.object({
  success: z.record(z.any()).describe('MUST provide the schema defining the structure of the response body for the specified MIME type. Follows JSON Schema specifications as per RFC 7159, enabling accurate data validation and formatting.'),
  example: z.record(z.any()).optional().describe('OPTIONAL. An example of the response body content for the specified MIME type. Provides practical illustrations of expected data formats and structures.'),
}).strict();

// Fields Schema
export const FieldsSchema = z.object({
  parameters: z.array(ParameterSchema).describe('MUST include an array of parameters that define the inputs required or accepted by the flow. These parameters serve as the interface for user-provided data, enabling dynamic and flexible flow interactions.'),
  requestBody: RequestBodySchema.optional().describe("OPTIONAL. Describes the structure of the request payload that the flow expects. Aligns with OpenAPI's `requestBody` specification as per RFC 7231, ensuring standardized data formats and communication."),
  responses: ResponsesSchema.describe('MUST be an object where that contains a `success` property that describes the response for a successful operation.'),
}).passthrough();

// Flow Schema
export const FlowSchema = z.object({
  id: z.string().describe('MUST provide a unique, human-readable identifier for the flow. Identifiers MUST be in snake_case format and globally unique within the `agents.json` context, ensuring clear reference and invocation. **Example**: `process_order_flow`'),
  title: z.string().describe('MUST provide the title of the flow. This title serves as a human-readable name for the flow, facilitating easy identification and selection.'),
  description: z.string().describe('MUST include a detailed description of the flow. This description should explain its purpose, the sequence of operations it performs, and its overall functionality. Essential for LLMs to determine the appropriate flow to execute based on user intent.'),
  actions: z.array(ActionSchema).describe('MUST include an array of actions that define the API operations to be executed in the flow. Each action corresponds to a specific API operation from a defined source, orchestrating the overall workflow.'),
  links: z.array(LinkSchema).optional().describe('MUST include an array of links that define how data flows between sources and destinations within the flow. Links connect data providers to data consumers, ensuring accurate data transfer.'),
  fields: FieldsSchema.describe('MUST define the parameters, request body, and responses for the flow. These fields serve as the interface for interaction with the flow, ensuring structured and clear data handling.'),
  additionalProperties: z.any().optional(),
}).passthrough();

// AgentsJson Schema
export const AgentsJsonSchema = z.object({
  agentsJson: z.string().describe('MUST specify the version of the `agents.json` specification being used. Adheres to Semantic Versioning (SemVer) as outlined at https://semver.org/.'),
  info: InfoSchema,
  sources: z.array(SourceSchema).describe('MUST include an array of API sources available for use within flows. Each source references an OpenAPI 3+ specification, enabling the chaining of multiple APIs.'),
  overrides: z.array(OverrideSchema).optional().describe('OPTIONAL. An array of overrides that allow customization of specific API operations. Overrides can modify fields within operations based on the specified `fieldPath`, enabling tailored behavior without altering the original API definitions.'),
  flows: z.array(FlowSchema).describe('MUST include an array of flows that define sequences of API operations to be executed. Each flow represents a cohesive workflow involving multiple actions, data links, and user interactions.'),
  additionalProperties: z.any().optional(),
}).passthrough();

// Export TypeScript types for usage
export type Info = z.infer<typeof InfoSchema>;
export type Source = z.infer<typeof SourceSchema>;
export type Override = z.infer<typeof OverrideSchema>;
export type Action = z.infer<typeof ActionSchema>;
export type Origin = z.infer<typeof OriginSchema>;
export type Target = z.infer<typeof TargetSchema>;
export type Link = z.infer<typeof LinkSchema>;
export type Parameter = z.infer<typeof ParameterSchema>;
export type Content = z.infer<typeof ContentSchema>;
export type RequestBody = z.infer<typeof RequestBodySchema>;
export type Responses = z.infer<typeof ResponsesSchema>;
export type Fields = z.infer<typeof FieldsSchema>;
export type Flow = z.infer<typeof FlowSchema>;
export type AgentsJson = z.infer<typeof AgentsJsonSchema>;
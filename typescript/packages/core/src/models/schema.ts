import { z } from 'zod';

// Info Schema
export const InfoSchema = z.object({
  title: z.string().describe('Title of the agents.json specification'),
  version: z.string().describe('Semantic version following SemVer format'),
  description: z.string().describe('Comprehensive description of the agents.json specification'),
}).strict();

export type Info = z.infer<typeof InfoSchema>;

// Source Schema
export const SourceSchema = z.object({
  id: z.string().describe('Unique identifier for the API source in snake_case format'),
  path: z.string().describe('File path or URL to the OpenAPI 3+ specification'),
}).strict();

export type Source = z.infer<typeof SourceSchema>;

// Override Schema
export const OverrideSchema = z.object({
  sourceId: z.string().describe('Must correspond to a source id'),
  operationId: z.string().describe('Must match an operationId in the OpenAPI spec'),
  fieldPath: z.string().describe('JSON path expression for the field to modify'),
  value: z.union([
    z.string(),
    z.record(z.any()),
    z.array(z.any()),
    z.boolean(),
    z.number(),
  ]).describe('New value for the specified field'),
}).strict();

export type Override = z.infer<typeof OverrideSchema>;

// Action Schema
export const ActionSchema = z.object({
  id: z.string().describe('Unique identifier for the action in snake_case format'),
  sourceId: z.string().describe('Reference to a source id'),
  operationId: z.string().describe('Operation identifier from the OpenAPI spec'),
}).strict();

export type Action = z.infer<typeof ActionSchema>;

// Origin Schema
export const OriginSchema = z.object({
  actionId: z.string().optional().describe('Optional identifier of the source action'),
  fieldPath: z.string().describe('JSON path expression for the source field'),
}).strict();

export type Origin = z.infer<typeof OriginSchema>;

// Target Schema
export const TargetSchema = z.object({
  actionId: z.string().optional().describe('Optional identifier of the target action'),
  fieldPath: z.string().describe('JSON path expression for the target field'),
}).strict();

export type Target = z.infer<typeof TargetSchema>;

// Link Schema
export const LinkSchema = z.object({
  origin: OriginSchema,
  target: TargetSchema,
}).strict();

export type Link = z.infer<typeof LinkSchema>;

// Parameter Schema
export const ParameterSchema = z.object({
  name: z.string().describe('Name of the parameter'),
  description: z.string().optional().describe('Optional description of the parameter'),
  required: z.boolean().default(false).describe('Whether the parameter is required'),
  type: z.string().optional().describe('Type of the parameter'),
}).strict();

export type Parameter = z.infer<typeof ParameterSchema>;

// Content Schema
export const ContentSchema = z.object({
  schema: z.record(z.any()).optional().describe('JSON Schema for the content'),
  example: z.record(z.any()).optional().describe('Example content'),
}).strict();

export type Content = z.infer<typeof ContentSchema>;

// RequestBody Schema
export const RequestBodySchema = z.object({
  content: z.record(ContentSchema).optional().describe('Map of MIME types to content schemas'),
  required: z.boolean().default(false).describe('Whether the request body is required'),
}).strict();

export type RequestBody = z.infer<typeof RequestBodySchema>;

// Responses Schema
export const ResponsesSchema = z.object({
  success: z.record(z.any()).describe('Schema for successful response'),
  example: z.record(z.any()).optional().describe('Example response'),
}).strict();

export type Responses = z.infer<typeof ResponsesSchema>;

// Fields Schema
export const FieldsSchema = z.object({
  parameters: z.array(ParameterSchema).describe('Array of flow parameters'),
  requestBody: RequestBodySchema.optional().describe('Optional request body structure'),
  responses: ResponsesSchema.describe('Response definitions'),
}).strict();

export type Fields = z.infer<typeof FieldsSchema>;

// Flow Schema
export const FlowSchema = z.object({
  id: z.string().describe('Unique identifier for the flow in snake_case format'),
  title: z.string().describe('Human-readable title of the flow'),
  description: z.string().describe('Detailed description of the flow'),
  actions: z.array(ActionSchema).describe('Array of actions to execute'),
  links: z.array(LinkSchema).optional().describe('Optional array of data flow links'),
  fields: FieldsSchema.describe('Interface definition for the flow'),
}).strict();

export type Flow = z.infer<typeof FlowSchema>;

// AgentsJson Schema
export const AgentsJsonSchema = z.object({
  agentsJson: z.string().describe('Version of the agents.json specification'),
  info: InfoSchema,
  sources: z.array(SourceSchema).describe('Array of API sources'),
  overrides: z.array(OverrideSchema).optional().describe('Optional array of API overrides'),
  flows: z.array(FlowSchema).describe('Array of workflow definitions'),
  additionalProperties: z.boolean().optional()
}).passthrough();

export type AgentsJson = z.infer<typeof AgentsJsonSchema>;

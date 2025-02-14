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

export interface Integration extends z.infer<typeof IntegrationSchema> {
  toTools(): Array<{
    name: string;
    description: string;
    parameters: z.ZodObject<any>;
    execute: (auth: Record<string, any>, params: Record<string, any>) => Promise<any>;
  }>;

  toMastraTools(authConfig: Record<string, any>): Record<string, Tool>;
}

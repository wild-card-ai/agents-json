import { AgentsJson } from './schema';

export interface Bundle {
  agentsJson: AgentsJson;
  openapi: Record<string, unknown>;
  operations: Record<string, unknown>;
  baseURL: string;
} 
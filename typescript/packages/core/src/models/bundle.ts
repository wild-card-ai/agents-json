import { AgentsJson } from './schema.js';

export interface Bundle {
  agentsJson: AgentsJson;
  openapi: Record<string, any>;
  operations: Record<string, any>;
}

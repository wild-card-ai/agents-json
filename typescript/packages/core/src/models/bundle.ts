import { AgentsJson } from '../../models/schema';

export interface Bundle {
  agentsJson: AgentsJson;
  openapi: Record<string, any>;
  operations: Record<string, any>;
}

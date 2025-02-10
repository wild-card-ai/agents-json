import { AuthConfig } from '../../types/auth';
import { initApiIntegration } from '../api-integration';
import { Bundle } from '../../types/bundle';
import { IntegrationModule } from '../../types/executor';

/**
 * Initialize Resend API integration
 * @param bundle The parsed agents.json bundle
 * @param auth Optional authentication configuration
 * @returns API map and executor type
 */
export async function createIntegration(bundle: Bundle, auth?: AuthConfig): Promise<IntegrationModule> {
  return initApiIntegration(bundle, { auth });
} 
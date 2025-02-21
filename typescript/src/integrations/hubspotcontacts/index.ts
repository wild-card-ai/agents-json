import { AuthConfig } from '../../types/auth';
import { initApiIntegration } from '../api-integration';
import { Bundle } from '../../types/bundle';
import { IntegrationModule } from '../../types/executor';

export async function createIntegration(bundle: Bundle, auth?: AuthConfig): Promise<IntegrationModule> {
  return initApiIntegration(bundle, { auth });
}
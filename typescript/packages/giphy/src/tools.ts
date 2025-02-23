import { Configuration, DefaultApi } from './client.js';

export class Executor {
  static createClient(apiKey: string): DefaultApi {
    const configuration = new Configuration(apiKey);
    return new DefaultApi(configuration);
  }

  static async runMethod(apiKey: string, methodName: string, params: Record<string, any> = {}): Promise<any> {
    const client = this.createClient(apiKey);
    const method = (client as any)[methodName];

    if (typeof method !== 'function') {
      throw new Error(`Unknown method: ${methodName}`);
    }

    console.log('Running method:', methodName, 'with params:', params);

    try {
      const response = await method.call(client, params);
      return response;
    } catch (error) {
      if (error instanceof Error) {
        throw new Error(`Giphy API error: ${error.message}`);
      }
      throw error;
    }
  }
}

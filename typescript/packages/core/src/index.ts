import { loadAgentsJson } from './loader.js';
import { Flow } from './models/schema.js';
import { toMastra } from './parsetools.js';

// Export models
export * from './models/schema.js';
export * from './models/auth.js';
export * from './models/bundle.js';

// Export core functionality
export * from './executor.js';
export * from './loader.js';

// Export utilities
export * from './utils.js';

export * from './parsetools.js';

export enum IntegrationType {
    RESTAPIHANDLER = "RESTAPIHANDLER",
    SDK = "SDK"
}

export class Integration {
    agentsJson: any;
    bundle: any;
    apiMap: any;
    constructor({
        agentsJson,
        apiMap,
    }: {
        agentsJson: any,
        apiMap: any,
    }) {
        this.agentsJson = agentsJson;
        this.apiMap = apiMap;
    }

    async initialize() {
        const bundle = await loadAgentsJson({
            url: this.agentsJson,
        });

        this.bundle = bundle;
    }

    toMastra(API_KEY: string) {
        const tools: Record<string, any> = {};
        this.bundle.agentsJson.flows.forEach((f: Flow) => {
            tools[f.id] = toMastra(f, this.apiMap, API_KEY);
        })
        return tools
    }
}
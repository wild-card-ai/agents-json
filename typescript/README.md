# @wildcard/agents-json

TypeScript implementation of the Agents.json specification with core functionality and integrations.

## Installation

```bash
npm install @wildcard/agents-json
```

## Features

- Core executor for running Agents.json flows
- REST API handler with support for various authentication methods
- Type-safe implementation using TypeScript and Zod
- Built-in integrations for popular services (coming soon)
  - Twitter
  - Giphy
  - Google Sheets
  - And more...

## Usage

### Basic Example

```typescript
import { execute, Bundle, Flow, AuthConfig, AuthType } from '@wildcard/agents-json';

// Define your bundle
const bundle: Bundle = {
  id: 'example-bundle',
  name: 'Example Bundle',
  flows: [
    {
      id: 'example-flow',
      actions: [
        {
          id: 'action1',
          sourceId: 'twitter',
          operationId: 'postTweet',
        },
      ],
    },
  ],
};

// Define your authentication
const auth: AuthConfig = {
  type: AuthType.OAUTH2,
  client_id: 'your-client-id',
  client_secret: 'your-client-secret',
  access_token: 'your-access-token',
};

// Execute the flow
const result = await execute(
  bundle,
  bundle.flows[0],
  auth,
  { text: 'Hello, World!' },
  {}
);
```

### Using the REST API Handler

```typescript
import { RestApiHandler } from '@wildcard/agents-json';

const api = new RestApiHandler({
  baseURL: 'https://api.example.com',
});

api.setAuth({
  type: AuthType.BEARER,
  token: 'your-token',
});

const response = await api.get('/endpoint', { param: 'value' });
```

## Development

```bash
# Install dependencies
npm install

# Build the package
npm run build

# Run tests
npm test

# Run type checking
npm run typecheck

# Run linting
npm run lint

# Format code
npm run format
```

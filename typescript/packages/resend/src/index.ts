import { IntegrationType, createIntegration } from '@agents-json/core';

// Generic REST API handler
interface ExecuteRequestParams {
  apiKey: string;
  method: string;
  path: string;
  body?: any;
}

const executeRequest = async ({
  apiKey,
  method,
  path,
  body
}: ExecuteRequestParams): Promise<any> => {
  const url = `https://api.resend.com${path}`;
  const response = await fetch(url, {
    method,
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json'
    },
    ...(body && { body: JSON.stringify(body) })
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({ message: response.statusText }));
    throw new Error(`Resend API error: ${error.message}`);
  }

  return response.json();
};

export const resendIntegration = createIntegration({
  id: 'resend',
  type: IntegrationType.REST,
  methods: {
    // Email Methods
    sendEmail: {
      name: 'sendEmail',
      description: 'Sends an email via the Resend API',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'from',
          type: 'string',
          description: 'Sender email address',
          required: true
        },
        {
          name: 'to',
          type: 'string',
          description: 'List of recipient email addresses (comma-separated)',
          required: true
        },
        {
          name: 'subject',
          type: 'string',
          description: 'Email subject',
          required: true
        },
        {
          name: 'html',
          type: 'string',
          description: 'HTML content of the email',
          required: false
        },
        {
          name: 'text',
          type: 'string',
          description: 'Plain text content of the email',
          required: false
        }
      ],
      execute: async (auth: { apiKey: string }, params: {
        from: string;
        to: string;
        subject: string;
        html?: string;
        text?: string;
      }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          method: 'POST',
          path: '/emails',
          body: {
            from: params.from,
            to: params.to.split(',').map(email => email.trim()),
            subject: params.subject,
            html: params.html,
            text: params.text
          }
        });
      }
    },

    getEmail: {
      name: 'getEmail',
      description: 'Retrieves email details using the email\'s unique ID',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'id',
          type: 'string',
          description: 'Email ID',
          required: true
        }
      ],
      execute: async (auth: { apiKey: string }, params: { id: string }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          method: 'GET',
          path: `/emails/${params.id}`
        });
      }
    },

    // Domain Methods
    createDomain: {
      name: 'createDomain',
      description: 'Creates a new domain',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'name',
          type: 'string',
          description: 'Domain name',
          required: true
        }
      ],
      execute: async (auth: { apiKey: string }, params: { name: string }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          method: 'POST',
          path: '/domains',
          body: { name: params.name }
        });
      }
    },

    getDomains: {
      name: 'getDomains',
      description: 'Lists all domains',
      type: IntegrationType.REST,
      parameters: [],
      execute: async (auth: { apiKey: string }, params: {}) => {
        return executeRequest({
          apiKey: auth.apiKey,
          method: 'GET',
          path: '/domains'
        });
      }
    },

    getDomain: {
      name: 'getDomain',
      description: 'Gets a specific domain',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'id',
          type: 'string',
          description: 'Domain ID',
          required: true
        }
      ],
      execute: async (auth: { apiKey: string }, params: { id: string }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          method: 'GET',
          path: `/domains/${params.id}`
        });
      }
    },

    verifyDomain: {
      name: 'verifyDomain',
      description: 'Verifies a domain',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'id',
          type: 'string',
          description: 'Domain ID',
          required: true
        }
      ],
      execute: async (auth: { apiKey: string }, params: { id: string }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          method: 'POST',
          path: `/domains/${params.id}/verify`
        });
      }
    },

    // Audience Methods
    createAudience: {
      name: 'createAudience',
      description: 'Creates a new audience',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'name',
          type: 'string',
          description: 'Audience name',
          required: true
        }
      ],
      execute: async (auth: { apiKey: string }, params: { name: string }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          method: 'POST',
          path: '/audiences',
          body: { name: params.name }
        });
      }
    },

    getAudiences: {
      name: 'getAudiences',
      description: 'Lists all audiences',
      type: IntegrationType.REST,
      parameters: [],
      execute: async (auth: { apiKey: string }, params: {}) => {
        return executeRequest({
          apiKey: auth.apiKey,
          method: 'GET',
          path: '/audiences'
        });
      }
    },

    getAudience: {
      name: 'getAudience',
      description: 'Gets a specific audience',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'id',
          type: 'string',
          description: 'Audience ID',
          required: true
        }
      ],
      execute: async (auth: { apiKey: string }, params: { id: string }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          method: 'GET',
          path: `/audiences/${params.id}`
        });
      }
    },

    // Contact Methods
    addContact: {
      name: 'addContact',
      description: 'Adds a contact to an audience',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'audienceId',
          type: 'string',
          description: 'Audience ID',
          required: true
        },
        {
          name: 'email',
          type: 'string',
          description: 'Contact email',
          required: true
        },
        {
          name: 'firstName',
          type: 'string',
          description: 'Contact first name',
          required: false
        },
        {
          name: 'lastName',
          type: 'string',
          description: 'Contact last name',
          required: false
        }
      ],
      execute: async (auth: { apiKey: string }, params: {
        audienceId: string;
        email: string;
        firstName?: string;
        lastName?: string;
      }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          method: 'POST',
          path: `/audiences/${params.audienceId}/contacts`,
          body: {
            email: params.email,
            first_name: params.firstName,
            last_name: params.lastName
          }
        });
      }
    },

    getContacts: {
      name: 'getContacts',
      description: 'Lists contacts in an audience',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'audienceId',
          type: 'string',
          description: 'Audience ID',
          required: true
        }
      ],
      execute: async (auth: { apiKey: string }, params: { audienceId: string }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          method: 'GET',
          path: `/audiences/${params.audienceId}/contacts`
        });
      }
    },

    // Broadcast Methods
    createBroadcast: {
      name: 'createBroadcast',
      description: 'Creates a new broadcast',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'name',
          type: 'string',
          description: 'Broadcast name',
          required: true
        },
        {
          name: 'audienceId',
          type: 'string',
          description: 'Audience ID',
          required: true
        },
        {
          name: 'subject',
          type: 'string',
          description: 'Email subject',
          required: true
        },
        {
          name: 'html',
          type: 'string',
          description: 'HTML content',
          required: false
        },
        {
          name: 'text',
          type: 'string',
          description: 'Text content',
          required: false
        }
      ],
      execute: async (auth: { apiKey: string }, params: {
        name: string;
        audienceId: string;
        subject: string;
        html?: string;
        text?: string;
      }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          method: 'POST',
          path: '/broadcasts',
          body: {
            name: params.name,
            audience_id: params.audienceId,
            subject: params.subject,
            html: params.html,
            text: params.text
          }
        });
      }
    },

    getBroadcasts: {
      name: 'getBroadcasts',
      description: 'Lists all broadcasts',
      type: IntegrationType.REST,
      parameters: [],
      execute: async (auth: { apiKey: string }, params: {}) => {
        return executeRequest({
          apiKey: auth.apiKey,
          method: 'GET',
          path: '/broadcasts'
        });
      }
    },

    getBroadcast: {
      name: 'getBroadcast',
      description: 'Gets a specific broadcast',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'id',
          type: 'string',
          description: 'Broadcast ID',
          required: true
        }
      ],
      execute: async (auth: { apiKey: string }, params: { id: string }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          method: 'GET',
          path: `/broadcasts/${params.id}`
        });
      }
    },

    sendBroadcast: {
      name: 'sendBroadcast',
      description: 'Sends a broadcast',
      type: IntegrationType.REST,
      parameters: [
        {
          name: 'id',
          type: 'string',
          description: 'Broadcast ID',
          required: true
        }
      ],
      execute: async (auth: { apiKey: string }, params: { id: string }) => {
        return executeRequest({
          apiKey: auth.apiKey,
          method: 'POST',
          path: `/broadcasts/${params.id}/send`
        });
      }
    }
  }
});

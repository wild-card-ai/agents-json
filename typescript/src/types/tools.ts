export enum ExecutorType {
  RESTAPIHANDLER = 'restapihandler',
  SDK = 'sdk',
}

export enum ToolFormat {
  OPENAI = 'openai',
  JSON = 'json',
}

export interface OpenAIToolCall {
  id: string;
  function: {
    name: string;
    arguments: string;
  };
}

export interface OpenAIResponse {
  choices: Array<{
    message: {
      tool_calls?: OpenAIToolCall[];
      content?: string;
    };
  }>;
} 
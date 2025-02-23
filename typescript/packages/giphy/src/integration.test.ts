
import { describe, it, expect } from 'vitest';
import { openai } from '@ai-sdk/openai';
import { Agent } from '@mastra/core/agent';
import { Giphy } from './integration';

describe('Giphy Integration', () => {
    it('Should generate', async () => {

        await Giphy.initialize();

        const giphyTools = Giphy.toMastra(process.env.GIPHY_API_KEY || '');

        const agent = new Agent({
            name: 'Giphy',
            instructions: `You get awesome gifs`,
            model: openai('gpt-4o'),
            tools: {
                ...giphyTools,
            }
        })

        const result = await agent.generate('What is a cool gif?')

        console.log(result)

        expect(result).toBeDefined();
    })
}, 30000);

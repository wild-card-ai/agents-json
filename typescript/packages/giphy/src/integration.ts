import { Integration } from "@agents-json/core";
import { map } from "./map";

export const Giphy = new Integration({
  agentsJson: 'https://raw.githubusercontent.com/wild-card-ai/agents-json/refs/heads/master/agents_json/giphy/agents.json',
  apiMap: map,
})
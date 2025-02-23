import { IntegrationType } from '@agents-json/core';
import { Executor } from './tools';

type MethodLambda = (apiKey: string, params?: Record<string, any>) => Promise<any>;

const getLambda = (methodName: string): MethodLambda => {
  return (apiKey: string, params: Record<string, any> = {}) =>
    Executor.runMethod(apiKey, methodName, params);
};

export const mapType = IntegrationType.SDK;

export const map: Record<string, MethodLambda> = {
  'giphy_get_gifs_trending': getLambda('giphy_get_gifs_trending'),
  'giphy_get_stickers_trending': getLambda('giphy_get_stickers_trending'),
  'giphy_get_gifs_search': getLambda('giphy_get_gifs_search'),
  'giphy_get_stickers_search': getLambda('giphy_get_stickers_search'),
  'giphy_get_gifs_translate': getLambda('giphy_get_gifs_translate'),
  'giphy_get_stickers_translate': getLambda('giphy_get_stickers_translate'),
  'giphy_get_gifs_random': getLambda('giphy_get_gifs_random'),
  'giphy_get_stickers_random': getLambda('giphy_get_stickers_random'),
  'giphy_get_randomid': getLambda('giphy_get_randomid'),
  'giphy_get_emoji': getLambda('giphy_get_emoji'),
  'giphy_get_emoji_variations_by_gif_id': getLambda('giphy_get_emoji_variations_by_gif_id'),
  'giphy_get_gifs_by_gif_id': getLambda('giphy_get_gifs_by_gif_id'),
  'giphy_get_gifs': getLambda('giphy_get_gifs'),
  'giphy_get_gifs_categories': getLambda('giphy_get_gifs_categories'),
  'giphy_get_gifs_search_tags': getLambda('giphy_get_gifs_search_tags'),
  'giphy_get_channels_search': getLambda('giphy_get_channels_search'),
  'giphy_get_tags_related_by_term': getLambda('giphy_get_tags_related_by_term'),
  'giphy_get_trending_searches': getLambda('giphy_get_trending_searches'),
};

from typing import Any, Callable, Dict
from .tools import Executor

def get_lambda(method_name: str) -> Callable[[], Dict[str, Any]]:
    return lambda api_key, **kwargs: Executor.run_method(api_key, method_name, **kwargs)

map = {
    'giphy_get_gifs_trending': get_lambda('giphy_get_gifs_trending'),
    'giphy_get_stickers_trending': get_lambda('giphy_get_stickers_trending'),
    'giphy_get_gifs_search': get_lambda('giphy_get_gifs_search'),
    'giphy_get_stickers_search': get_lambda('giphy_get_stickers_search'),
    'giphy_get_gifs_translate': get_lambda('giphy_get_gifs_translate'),
    'giphy_get_stickers_translate': get_lambda('giphy_get_stickers_translate'),
    'giphy_get_gifs_random': get_lambda('giphy_get_gifs_random'),
    'giphy_get_stickers_random': get_lambda('giphy_get_stickers_random'),
    'giphy_get_randomid': get_lambda('giphy_get_randomid'),
    'giphy_get_emoji': get_lambda('giphy_get_emoji'),
    'giphy_get_emoji_variations_by_gif_id': get_lambda('giphy_get_emoji_variations_by_gif_id'),
    'giphy_get_gifs_by_gif_id': get_lambda('giphy_get_gifs_by_gif_id'),
    'giphy_get_gifs': get_lambda('giphy_get_gifs'),
    'giphy_get_gifs_categories': get_lambda('giphy_get_gifs_categories'),
    'giphy_get_gifs_search_tags': get_lambda('giphy_get_gifs_search_tags'),
    'giphy_get_channels_search': get_lambda('giphy_get_channels_search'),
    'giphy_get_tags_related_by_term': get_lambda('giphy_get_tags_related_by_term'),
    'giphy_get_trending_searches': get_lambda('giphy_get_trending_searches'),
}
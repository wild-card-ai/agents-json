from typing import Any, Callable, Dict
from .tools import RestApiHandler, AlpacaApiType
from ..types import ExecutorType

map_type = ExecutorType.RESTAPIHANDLER

# Mapping dictionary that defines the HTTP method, resource path, and API type
OPERATION_MAPPING: Dict[str, tuple[str, str, AlpacaApiType]] = {
    # Trading API Operations
    "alpacatrading_get_account": ("GET", "/v2/account", AlpacaApiType.TRADING),
    "alpacatrading_post_order": ("POST", "/v2/orders", AlpacaApiType.TRADING),
    "alpacatrading_get_all_orders": ("GET", "/v2/orders", AlpacaApiType.TRADING),
    "alpacatrading_delete_all_orders": ("DELETE", "/v2/orders", AlpacaApiType.TRADING),
    "alpacatrading_get_order_by_order_i_d": ("GET", "/v2/orders/{order_id}", AlpacaApiType.TRADING),
    "alpacatrading_patch_order_by_order_id": ("PATCH", "/v2/orders/{order_id}", AlpacaApiType.TRADING),
    "alpacatrading_delete_order_by_order_i_d": ("DELETE", "/v2/orders/{order_id}", AlpacaApiType.TRADING),
    "alpacatrading_get_all_open_positions": ("GET", "/v2/positions", AlpacaApiType.TRADING),
    "alpacatrading_delete_all_open_positions": ("DELETE", "/v2/positions", AlpacaApiType.TRADING),
    "alpacatrading_get_open_position": ("GET", "/v2/positions/{symbol_or_asset_id}", AlpacaApiType.TRADING),
    "alpacatrading_delete_open_position": ("DELETE", "/v2/positions/{symbol_or_asset_id}", AlpacaApiType.TRADING),
    "alpacatrading_option_exercise": ("POST", "/v2/positions/{symbol_or_contract_id}/exercise", AlpacaApiType.TRADING),
    "alpacatrading_get_account_portfolio_history": ("GET", "/v2/account/portfolio/history", AlpacaApiType.TRADING),
    "alpacatrading_get_watchlists": ("GET", "/v2/watchlists", AlpacaApiType.TRADING),
    "alpacatrading_post_watchlist": ("POST", "/v2/watchlists", AlpacaApiType.TRADING),
    "alpacatrading_get_watchlist_by_id": ("GET", "/v2/watchlists/{watchlist_id}", AlpacaApiType.TRADING),
    "alpacatrading_update_watchlist_by_id": ("PUT", "/v2/watchlists/{watchlist_id}", AlpacaApiType.TRADING),
    "alpacatrading_add_asset_to_watchlist": ("POST", "/v2/watchlists/{watchlist_id}", AlpacaApiType.TRADING),
    "alpacatrading_delete_watchlist_by_id": ("DELETE", "/v2/watchlists/{watchlist_id}", AlpacaApiType.TRADING),
    "alpacatrading_get_watchlist_by_name": ("GET", "/v2/watchlists:by_name", AlpacaApiType.TRADING),
    "alpacatrading_update_watchlist_by_name": ("PUT", "/v2/watchlists:by_name", AlpacaApiType.TRADING),
    "alpacatrading_add_asset_to_watchlist_by_name": ("POST", "/v2/watchlists:by_name", AlpacaApiType.TRADING),
    "alpacatrading_delete_watchlist_by_name": ("DELETE", "/v2/watchlists:by_name", AlpacaApiType.TRADING),
    "alpacatrading_remove_asset_from_watchlist": ("DELETE", "/v2/watchlists/{watchlist_id}/{symbol}", AlpacaApiType.TRADING),
    "alpacatrading_get_account_config": ("GET", "/v2/account/configurations", AlpacaApiType.TRADING),
    "alpacatrading_patch_account_config": ("PATCH", "/v2/account/configurations", AlpacaApiType.TRADING),
    "alpacatrading_get_account_activities": ("GET", "/v2/account/activities", AlpacaApiType.TRADING),
    "alpacatrading_get_account_activities_by_activity_type": ("GET", "/v2/account/activities/{activity_type}", AlpacaApiType.TRADING),
    "alpacatrading_get_calendar": ("GET", "/v2/calendar", AlpacaApiType.TRADING),
    "alpacatrading_get_clock": ("GET", "/v2/clock", AlpacaApiType.TRADING),
    "alpacatrading_get-v2-assets": ("GET", "/v2/assets", AlpacaApiType.TRADING),
    "alpacatrading_get-v2-assets-symbol_or_asset_id": ("GET", "/v2/assets/{symbol_or_asset_id}", AlpacaApiType.TRADING),
    "alpacatrading_get-options-contracts": ("GET", "/v2/options/contracts", AlpacaApiType.TRADING),
    "alpacatrading_get-option-contract-symbol_or_id": ("GET", "/v2/options/contracts/{symbol_or_id}", AlpacaApiType.TRADING),
    "alpacatrading_get-v2-corporate_actions-announcements-id": ("GET", "/v2/corporate_actions/announcements/{id}", AlpacaApiType.TRADING),
    "alpacatrading_get-v2-corporate_actions-announcements": ("GET", "/v2/corporate_actions/announcements", AlpacaApiType.TRADING),
    "alpacatrading_list_crypto_funding_wallets": ("GET", "/v2/wallets", AlpacaApiType.TRADING),
    "alpacatrading_list_crypto_funding_transfers": ("GET", "/v2/wallets/transfers", AlpacaApiType.TRADING),
    "alpacatrading_create_crypto_transfer_for_account": ("POST", "/v2/wallets/transfers", AlpacaApiType.TRADING),
    "alpacatrading_get_crypto_funding_transfer": ("GET", "/v2/wallets/transfers/{transfer_id}", AlpacaApiType.TRADING),
    "alpacatrading_list_whitelisted_address": ("GET", "/v2/wallets/whitelists", AlpacaApiType.TRADING),
    "alpacatrading_create_whitelisted_address": ("POST", "/v2/wallets/whitelists", AlpacaApiType.TRADING),
    "alpacatrading_delete_whitelisted_address": ("DELETE", "/v2/wallets/whitelists/{whitelisted_address_id}", AlpacaApiType.TRADING),
    "alpacatrading_get_crypto_transfer_estimate": ("GET", "/v2/wallets/fees/estimate", AlpacaApiType.TRADING),

    # Market Data API Operations
    "alpacamarketdata_corporate_actions": ("GET", "/v1/corporate-actions", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_latest_rates": ("GET", "/v1beta1/forex/latest/rates", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_rates": ("GET", "/v1beta1/forex/rates", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_logos": ("GET", "/v1beta1/logos/{symbol}", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_news": ("GET", "/v1beta1/news", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_option_bars": ("GET", "/v1beta1/options/bars", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_option_meta_conditions": ("GET", "/v1beta1/options/meta/conditions/{ticktype}", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_option_meta_exchanges": ("GET", "/v1beta1/options/meta/exchanges", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_option_latest_quotes": ("GET", "/v1beta1/options/quotes/latest", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_option_snapshots": ("GET", "/v1beta1/options/snapshots", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_option_chain": ("GET", "/v1beta1/options/snapshots/{underlying_symbol}", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_option_trades": ("GET", "/v1beta1/options/trades", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_option_latest_trades": ("GET", "/v1beta1/options/trades/latest", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_most_actives": ("GET", "/v1beta1/screener/stocks/most-actives", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_movers": ("GET", "/v1beta1/screener/{market_type}/movers", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_crypto_perp_latest_bars": ("GET", "/v1beta1/crypto-perps/{loc}/latest/bars", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_crypto_perp_latest_orderbooks": ("GET", "/v1beta1/crypto-perps/{loc}/latest/orderbooks", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_crypto_perp_latest_quotes": ("GET", "/v1beta1/crypto-perps/{loc}/latest/quotes", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_crypto_perp_latest_trades": ("GET", "/v1beta1/crypto-perps/{loc}/latest/trades", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_crypto_bars": ("GET", "/v1beta3/crypto/{loc}/bars", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_crypto_latest_bars": ("GET", "/v1beta3/crypto/{loc}/latest/bars", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_crypto_latest_orderbooks": ("GET", "/v1beta3/crypto/{loc}/latest/orderbooks", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_crypto_latest_quotes": ("GET", "/v1beta3/crypto/{loc}/latest/quotes", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_crypto_latest_trades": ("GET", "/v1beta3/crypto/{loc}/latest/trades", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_crypto_quotes": ("GET", "/v1beta3/crypto/{loc}/quotes", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_crypto_snapshots": ("GET", "/v1beta3/crypto/{loc}/snapshots", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_crypto_trades": ("GET", "/v1beta3/crypto/{loc}/trades", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_stock_auctions": ("GET", "/v2/stocks/auctions", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_stock_bars": ("GET", "/v2/stocks/bars", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_stock_latest_bars": ("GET", "/v2/stocks/bars/latest", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_stock_meta_conditions": ("GET", "/v2/stocks/meta/conditions/{ticktype}", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_stock_meta_exchanges": ("GET", "/v2/stocks/meta/exchanges", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_stock_quotes": ("GET", "/v2/stocks/quotes", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_stock_latest_quotes": ("GET", "/v2/stocks/quotes/latest", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_stock_snapshots": ("GET", "/v2/stocks/snapshots", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_stock_trades": ("GET", "/v2/stocks/trades", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_stock_latest_trades": ("GET", "/v2/stocks/trades/latest", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_stock_auction_single": ("GET", "/v2/stocks/{symbol}/auctions", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_stock_bar_single": ("GET", "/v2/stocks/{symbol}/bars", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_stock_latest_bar_single": ("GET", "/v2/stocks/{symbol}/bars/latest", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_stock_quote_single": ("GET", "/v2/stocks/{symbol}/quotes", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_stock_latest_quote_single": ("GET", "/v2/stocks/{symbol}/quotes/latest", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_stock_snapshot_single": ("GET", "/v2/stocks/{symbol}/snapshot", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_stock_trade_single": ("GET", "/v2/stocks/{symbol}/trades", AlpacaApiType.MARKET_DATA),
    "alpacamarketdata_stock_latest_trade_single": ("GET", "/v2/stocks/{symbol}/trades/latest", AlpacaApiType.MARKET_DATA),
}

def get_lambda(operation_id: str) -> Callable[[str], Dict[str, Any]]:
    """
    Creates a lambda function that executes a REST API call for the given operation.
    
    :param operation_id: The operation ID (e.g. "alpacatrading_post_order")
    :return: A lambda that takes an auth_config and kwargs, executing the appropriate REST call
    """
    if operation_id not in OPERATION_MAPPING:
        raise ValueError(f"Operation id {operation_id} not supported")
    
    method, resource_path, api_type = OPERATION_MAPPING[operation_id]
    
    # The lambda extracts parameters and request_body from kwargs and passes them to RestApiHandler
    return lambda auth_config, **kwargs: RestApiHandler.execute(
        auth_config=auth_config,
        method=method,
        resource_path=resource_path,
        parameters=kwargs.get("parameters", {}),
        request_body=kwargs.get("requestBody", kwargs.get("request_body", {})),
        api_type=api_type
    )

# Generate the mapping dynamically based on the operation mapping dictionary
map = {op_id: get_lambda(op_id) for op_id in OPERATION_MAPPING}

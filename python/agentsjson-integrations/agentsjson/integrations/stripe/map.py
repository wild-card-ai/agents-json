
from .tools import Executor

map = {
    "stripe_post_customers": Executor.stripe_post_customers,
    "stripe_get_customers": Executor.stripe_get_customers,
    "stripe_post_products": Executor.stripe_post_products,
    "stripe_get_products": Executor.stripe_get_products,
    "stripe_post_prices": Executor.stripe_post_prices,
    "stripe_get_prices": Executor.stripe_get_prices,
    "stripe_post_payment_links": Executor.stripe_post_payment_links,
    "stripe_post_invoices": Executor.stripe_post_invoices,
    "stripe_post_invoiceitems": Executor.stripe_post_invoiceitems,
    "stripe_post_invoices_invoice_finalize": Executor.stripe_post_invoices_invoice_finalize,
    "stripe_get_balance": Executor.stripe_get_balance,
    "stripe_post_refunds": Executor.stripe_post_refunds,
    "stripe_post_products_id": Executor.stripe_post_products_id,
    "stripe_get_products_id": Executor.stripe_get_products_id,
    "stripe_post_checkout_sessions": Executor.stripe_post_checkout_sessions,
    "stripe_post_billing_portal_sessions": Executor.stripe_post_billing_portal_sessions,
    "stripe_get_prices_price": Executor.stripe_get_prices_price,
    "stripe_post_prices_price": Executor.stripe_post_prices_price,
    "stripe_get_customers_search": Executor.stripe_get_customers_search,
    "stripe_get_customers_customer": Executor.stripe_get_customers_customer,
    "stripe_get_billing_portal_configurations": Executor.stripe_get_billing_portal_configurations,
    "stripe_post_billing_portal_configurations": Executor.stripe_post_billing_portal_configurations
}
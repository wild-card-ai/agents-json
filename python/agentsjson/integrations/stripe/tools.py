from pydantic import BaseModel

class Executor(BaseModel):
    @staticmethod
    def stripe_post_customers(api_key: str, **kwargs):
        import stripe
        stripe.api_key = api_key
        return stripe.Customer.create(**kwargs)

    @staticmethod
    def stripe_get_customers(api_key: str, **kwargs):
        import stripe
        stripe.api_key = api_key
        return stripe.Customer.list(**kwargs)

    @staticmethod
    def stripe_post_products(api_key: str, **kwargs):
        import stripe
        stripe.api_key = api_key
        return stripe.Product.create(**kwargs)

    @staticmethod
    def stripe_get_products(api_key: str, **kwargs):
        import stripe
        stripe.api_key = api_key
        return stripe.Product.list(**kwargs)

    @staticmethod
    def stripe_post_prices(api_key: str, **kwargs):
        import stripe
        stripe.api_key = api_key
        return stripe.Price.create(**kwargs)

    @staticmethod
    def stripe_get_prices(api_key: str, **kwargs):
        import stripe
        stripe.api_key = api_key
        return stripe.Price.list(**kwargs)

    @staticmethod
    def stripe_post_payment_links(api_key: str, **kwargs):
        import stripe
        stripe.api_key = api_key
        return stripe.PaymentLink.create(**kwargs)

    @staticmethod
    def stripe_post_invoices(api_key: str, **kwargs):
        import stripe
        stripe.api_key = api_key
        return stripe.Invoice.create(**kwargs)

    @staticmethod
    def stripe_post_invoiceitems(api_key: str, **kwargs):
        import stripe
        stripe.api_key = api_key
        return stripe.InvoiceItem.create(**kwargs)

    @staticmethod
    def stripe_post_invoices_invoice_finalize(api_key: str, invoice_id, **kwargs):
        import stripe
        stripe.api_key = api_key
        invoice = stripe.Invoice.retrieve(invoice_id)
        return invoice.finalize_invoice(**kwargs)

    @staticmethod
    def stripe_get_balance(api_key: str, **kwargs):
        import stripe
        stripe.api_key = api_key
        return stripe.Balance.retrieve(**kwargs)

    @staticmethod
    def stripe_post_refunds(api_key: str, **kwargs):
        import stripe
        stripe.api_key = api_key
        return stripe.Refund.create(**kwargs)
            
    @staticmethod
    def stripe_post_products_id(api_key: str, id, **kwargs):
        import stripe
        stripe.api_key = api_key
        product = stripe.Product.modify(id, **kwargs)
        return product

    @staticmethod
    def stripe_get_products_id(api_key: str, id, **kwargs):
        import stripe
        stripe.api_key = api_key
        return stripe.Product.retrieve(id)

    @staticmethod
    def stripe_post_checkout_sessions(api_key: str, **kwargs):
        import stripe
        stripe.api_key = api_key
        return stripe.checkout.Session.create(**kwargs)

    @staticmethod
    def stripe_post_billing_portal_sessions(api_key: str, **kwargs):
        import stripe
        stripe.api_key = api_key
        return stripe.billing_portal.Session.create(**kwargs)

    @staticmethod
    def stripe_get_prices_price(api_key: str, price, **kwargs):
        import stripe
        stripe.api_key = api_key
        return stripe.Price.retrieve(price, **kwargs)

    @staticmethod
    def stripe_post_prices_price(api_key: str, price, **kwargs):
        import stripe
        stripe.api_key = api_key
        return stripe.Price.modify(price, **kwargs)

    @staticmethod
    def stripe_get_customers_search(api_key: str, **kwargs):
        import stripe
        stripe.api_key = api_key
        return stripe.Customer.search(**kwargs)

    @staticmethod
    def stripe_get_customers_customer(api_key: str, customer, **kwargs):
        import stripe
        stripe.api_key = api_key
        return stripe.Customer.retrieve(customer, **kwargs)

    @staticmethod
    def stripe_get_billing_portal_configurations(api_key: str, **kwargs):
        import stripe
        stripe.api_key = api_key
        return stripe.billing_portal.Configuration.list(**kwargs)

    @staticmethod
    def stripe_post_billing_portal_configurations(api_key: str, **kwargs):
        import stripe
        stripe.api_key = api_key
        return stripe.billing_portal.Configuration.create(**kwargs)
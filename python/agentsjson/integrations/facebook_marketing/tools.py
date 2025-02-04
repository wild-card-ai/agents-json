from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.ad import Ad

class Executor:
    @staticmethod
    def facebookmarketing_get_campaigns(api_key: str, ad_account_id: str, **kwargs):
        FacebookAdsApi.init(access_token=api_key)
        account = AdAccount("act_" + ad_account_id)
        return account.get_campaigns(params=kwargs)

    @staticmethod
    def facebookmarketing_create_campaign(api_key: str, ad_account_id: str, properties: dict, **kwargs):
        FacebookAdsApi.init(access_token=api_key)
        account = AdAccount("act_" + ad_account_id)
        params = {**properties, **kwargs}
        return account.create_campaign(params=params)

    @staticmethod
    def facebookmarketing_update_campaign(api_key: str, campaign_id: str, properties: dict, **kwargs):
        FacebookAdsApi.init(access_token=api_key)
        campaign = Campaign(campaign_id)
        params = {**properties, **kwargs}
        return campaign.api_update(params=params)

    @staticmethod
    def facebookmarketing_dissociate_campaign(api_key: str, ad_account_id: str, campaign_id: str, **kwargs):
        # In this example, dissociation is implemented as removal (deletion) of the campaign association.
        FacebookAdsApi.init(access_token=api_key)
        campaign = Campaign(campaign_id)
        return campaign.api_delete(params=kwargs)

    @staticmethod
    def facebookmarketing_delete_campaign(api_key: str, campaign_id: str, **kwargs):
        FacebookAdsApi.init(access_token=api_key)
        campaign = Campaign(campaign_id)
        return campaign.api_delete(params=kwargs)

    @staticmethod
    def facebookmarketing_get_ad_sets(api_key: str, ad_account_id: str, **kwargs):
        FacebookAdsApi.init(access_token=api_key)
        account = AdAccount("act_" + ad_account_id)
        return account.get_ad_sets(params=kwargs)

    @staticmethod
    def facebookmarketing_create_ad_set(api_key: str, ad_account_id: str, properties: dict, **kwargs):
        FacebookAdsApi.init(access_token=api_key)
        account = AdAccount("act_" + ad_account_id)
        params = {**properties, **kwargs}
        return account.create_ad_set(params=params)

    @staticmethod
    def facebookmarketing_get_ad_set(api_key: str, ad_set_id: str, **kwargs):
        FacebookAdsApi.init(access_token=api_key)
        ad_set = AdSet(ad_set_id)
        return ad_set.api_get(params=kwargs)

    @staticmethod
    def facebookmarketing_update_ad_set(api_key: str, ad_set_id: str, properties: dict, **kwargs):
        FacebookAdsApi.init(access_token=api_key)
        ad_set = AdSet(ad_set_id)
        params = {**properties, **kwargs}
        return ad_set.api_update(params=params)

    @staticmethod
    def facebookmarketing_delete_ad_set(api_key: str, ad_set_id: str, **kwargs):
        FacebookAdsApi.init(access_token=api_key)
        ad_set = AdSet(ad_set_id)
        return ad_set.api_delete(params=kwargs)

    @staticmethod
    def facebookmarketing_get_ads(api_key: str, ad_account_id: str, **kwargs):
        FacebookAdsApi.init(access_token=api_key)
        account = AdAccount("act_" + ad_account_id)
        return account.get_ads(params=kwargs)

    @staticmethod
    def facebookmarketing_create_ad(api_key: str, ad_account_id: str, properties: dict, **kwargs):
        FacebookAdsApi.init(access_token=api_key)
        account = AdAccount("act_" + ad_account_id)
        params = {**properties, **kwargs}
        return account.create_ad(params=params)

    @staticmethod
    def facebookmarketing_get_ad(api_key: str, ad_id: str, **kwargs):
        FacebookAdsApi.init(access_token=api_key)
        ad = Ad(ad_id)
        return ad.api_get(params=kwargs)

    @staticmethod
    def facebookmarketing_update_ad(api_key: str, ad_id: str, properties: dict, **kwargs):
        FacebookAdsApi.init(access_token=api_key)
        ad = Ad(ad_id)
        params = {**properties, **kwargs}
        return ad.api_update(params=params)

    @staticmethod
    def facebookmarketing_delete_ad(api_key: str, ad_id: str, **kwargs):
        FacebookAdsApi.init(access_token=api_key)
        ad = Ad(ad_id)
        return ad.api_delete(params=kwargs)

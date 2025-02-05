from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from functools import lru_cache
from hubspot import HubSpot
from hubspot.crm.contacts import (
    SimplePublicObjectInput,
    SimplePublicObjectInputForCreate,
    BatchInputSimplePublicObjectId,
    BatchInputSimplePublicObjectInputForCreate,
    BatchInputSimplePublicObjectBatchInput,
    PublicGdprDeleteInput,
    PublicMergeInput,
    PublicObjectSearchRequest,
)
from ...core.models.auth import OAuth2AuthConfig

class Executor(BaseModel):
    """
    Executor class for HubSpot Contacts API operations.
    
    Authentication is handled via OAuth2 configuration which should be provided as a separate parameter.
    The OAuth2 config should contain the access token and optional refresh token obtained through the OAuth 2.0 flow.
    """
    
    @staticmethod
    @lru_cache(maxsize=100)  # Cache up to 100 client instances
    def _get_hubspot_client(auth_config: OAuth2AuthConfig) -> HubSpot:
        """
        Creates a HubSpot client using OAuth2 authentication.
        This function is cached with LRU policy.
        """
        return HubSpot(access_token=auth_config.token)

    @staticmethod
    def hubspotcontacts_list_contacts(auth_config: OAuth2AuthConfig, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        client = Executor._get_hubspot_client(auth_config)
        
        # Extract array fields from requestBody if present
        request_body = kwargs.pop('requestBody', {})
        
        # Convert array parameters to comma-separated strings as required by HubSpot API
        if 'properties' in request_body:
            kwargs['properties'] = ','.join(request_body['properties'])
        if 'propertiesWithHistory' in request_body:
            kwargs['propertiesWithHistory'] = ','.join(request_body['propertiesWithHistory'])
        if 'associations' in request_body:
            kwargs['associations'] = ','.join(request_body['associations'])
            
        return client.crm.contacts.basic_api.get_page(**kwargs)

    @staticmethod
    def hubspotcontacts_create_contact(auth_config: OAuth2AuthConfig, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        properties = kwargs.get("properties", {})
        associations = kwargs.get("associations", [])
        
        client = Executor._get_hubspot_client(auth_config)
        data = SimplePublicObjectInputForCreate(
            properties=properties,
            associations=associations
        )
        return client.crm.contacts.basic_api.create(
            simple_public_object_input_for_create=data
        )

    @staticmethod
    def hubspotcontacts_batch_archive_contacts(auth_config: OAuth2AuthConfig, kwargs: Dict[str, Any]) -> None:
        contact_ids = kwargs["contact_ids"]
        
        client = Executor._get_hubspot_client(auth_config)
        data = BatchInputSimplePublicObjectId(
            inputs=[{"id": id} for id in contact_ids]
        )
        client.crm.contacts.batch_api.archive(batch_input_simple_public_object_id=data)

    @staticmethod
    def hubspotcontacts_batch_create_contacts(auth_config: OAuth2AuthConfig, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        contacts = kwargs["contacts"]
        
        client = Executor._get_hubspot_client(auth_config)
        data = BatchInputSimplePublicObjectInputForCreate(
            inputs=[
                SimplePublicObjectInputForCreate(
                    properties=contact.get("properties", {}),
                    associations=contact.get("associations", [])
                ) for contact in contacts
            ]
        )
        return client.crm.contacts.batch_api.create(
            batch_input_simple_public_object_input_for_create=data
        )

    @staticmethod
    def hubspotcontacts_batch_read_contacts(auth_config: OAuth2AuthConfig, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        contact_ids = kwargs["contact_ids"]
        
        client = Executor._get_hubspot_client(auth_config)
        data = BatchInputSimplePublicObjectId(
            inputs=[{"id": id} for id in contact_ids]
        )
        return client.crm.contacts.batch_api.read(
            batch_input_simple_public_object_id=data,
            **kwargs
        )

    @staticmethod
    def hubspotcontacts_batch_update_contacts(auth_config: OAuth2AuthConfig, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        contacts = kwargs["contacts"]
        
        client = Executor._get_hubspot_client(auth_config)
        data = BatchInputSimplePublicObjectBatchInput(
            inputs=[{
                "id": contact["id"],
                "properties": contact["properties"]
            } for contact in contacts]
        )
        return client.crm.contacts.batch_api.update(
            batch_input_simple_public_object_batch_input=data
        )

    @staticmethod
    def hubspotcontacts_gdpr_delete_contacts(auth_config: OAuth2AuthConfig, kwargs: Dict[str, Any]) -> None:
        object_id = kwargs["object_id"]
        id_property = kwargs.get("id_property")
        
        client = Executor._get_hubspot_client(auth_config)
        data = PublicGdprDeleteInput(
            object_id=object_id,
            id_property=id_property
        )
        client.crm.contacts.gdpr_api.purge(
            public_gdpr_delete_input=data
        )

    @staticmethod
    def hubspotcontacts_merge_contacts(auth_config: OAuth2AuthConfig, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        primary_object_id = kwargs["primary_object_id"]
        object_id_to_merge = kwargs["object_id_to_merge"]
        
        client = Executor._get_hubspot_client(auth_config)
        data = PublicMergeInput(
            primary_object_id=primary_object_id,
            object_id_to_merge=object_id_to_merge
        )
        return client.crm.contacts.public_object_api.merge(
            public_merge_input=data
        )

    @staticmethod
    def hubspotcontacts_search_contacts(auth_config: OAuth2AuthConfig, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        client = Executor._get_hubspot_client(auth_config)
        data = PublicObjectSearchRequest(**kwargs)
        return client.crm.contacts.search_api.do_search(
            public_object_search_request=data
        )

    @staticmethod
    def hubspotcontacts_get_contact(auth_config: OAuth2AuthConfig, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        contact_id = kwargs.pop("contact_id")
        
        client = Executor._get_hubspot_client(auth_config)
        return client.crm.contacts.basic_api.get_by_id(
            contact_id=contact_id,
            **kwargs
        )

    @staticmethod
    def hubspotcontacts_archive_contact(auth_config: OAuth2AuthConfig, kwargs: Dict[str, Any]) -> None:
        contact_id = kwargs["contact_id"]
        
        client = Executor._get_hubspot_client(auth_config)
        client.crm.contacts.basic_api.archive(contact_id=contact_id)

    @staticmethod
    def hubspotcontacts_update_contact(auth_config: OAuth2AuthConfig, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        contact_id = kwargs["contact_id"]
        properties = kwargs["properties"]
        
        client = Executor._get_hubspot_client(auth_config)
        data = SimplePublicObjectInput(properties=properties)
        return client.crm.contacts.basic_api.update(
            contact_id=contact_id,
            simple_public_object_input=data
        )

from typing import Dict, Callable, Any
from .tools import Executor
from ..types import ExecutorType

map_type = ExecutorType.SDK

map: Dict[str, Callable[..., Any]] = {
    "hubspotcontacts_list_contacts": Executor.hubspotcontacts_list_contacts,
    "hubspotcontacts_create_contact": Executor.hubspotcontacts_create_contact,
    "hubspotcontacts_batch_archive_contacts": Executor.hubspotcontacts_batch_archive_contacts,
    "hubspotcontacts_batch_create_contacts": Executor.hubspotcontacts_batch_create_contacts,
    "hubspotcontacts_batch_read_contacts": Executor.hubspotcontacts_batch_read_contacts,
    "hubspotcontacts_batch_update_contacts": Executor.hubspotcontacts_batch_update_contacts,
    # "hubspotcontacts_gdpr_delete_contacts": Executor.hubspotcontacts_gdpr_delete_contacts,
    "hubspotcontacts_merge_contacts": Executor.hubspotcontacts_merge_contacts,
    "hubspotcontacts_search_contacts": Executor.hubspotcontacts_search_contacts,
    "hubspotcontacts_get_contact": Executor.hubspotcontacts_get_contact,
    "hubspotcontacts_archive_contact": Executor.hubspotcontacts_archive_contact,
    "hubspotcontacts_update_contact": Executor.hubspotcontacts_update_contact,
}

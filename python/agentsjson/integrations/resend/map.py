from typing import Any, Callable, Dict
from .tools import Executor

def get_lambda(method_name: str) -> Callable[[str], Dict[str, Any]]:
    return lambda api_key, **kwargs: Executor.run_method(api_key, method_name, **kwargs)

OPERATION_IDS = [
    "resend_post_emails",  # POST /emails
    "resend_get_emails_by_email_id",  # GET /emails/{email_id}
    "resend_patch_emails_by_email_id",  # PATCH /emails/{email_id}
    "resend_post_emails_cancel_by_email_id",  # POST /emails/{email_id}/cancel
    "resend_post_emails_batch",  # POST /emails/batch
    "resend_post_domains",  # POST /domains
    "resend_get_domains",  # GET /domains
    "resend_get_domains_by_domain_id",  # GET /domains/{domain_id}
    "resend_patch_domains_by_domain_id",  # PATCH /domains/{domain_id}
    "resend_delete_domains_by_domain_id",  # DELETE /domains/{domain_id}
    "resend_post_domains_verify_by_domain_id",  # POST /domains/{domain_id}/verify
    "resend_post_api_keys",  # POST /api-keys
    "resend_get_api_keys",  # GET /api-keys
    "resend_delete_api_keys_by_api_key_id",  # DELETE /api-keys/{api_key_id}
    "resend_post_audiences",  # POST /audiences
    "resend_get_audiences",  # GET /audiences
    "resend_delete_audiences_by_id",  # DELETE /audiences/{id}
    "resend_get_audiences_by_id",  # GET /audiences/{id}
    "resend_post_audiences_contacts_by_audience_id",  # POST /audiences/{audience_id}/contacts
    "resend_get_audiences_contacts_by_audience_id",  # GET /audiences/{audience_id}/contacts
    "resend_delete_audiences_contacts_by_audience_id_and_email",  # DELETE /audiences/{audience_id}/contacts/{email}
    "resend_delete_audiences_contacts_by_audience_id_and_id",  # DELETE /audiences/{audience_id}/contacts/{id}
    "resend_get_audiences_contacts_by_audience_id_and_id",  # GET /audiences/{audience_id}/contacts/{id}
    "resend_patch_audiences_contacts_by_audience_id_and_id",  # PATCH /audiences/{audience_id}/contacts/{id}
    "resend_post_broadcasts",  # POST /broadcasts
    "resend_get_broadcasts",  # GET /broadcasts
    "resend_delete_broadcasts_by_id",  # DELETE /broadcasts/{id}
    "resend_get_broadcasts_by_id",  # GET /broadcasts/{id}
    "resend_post_broadcasts_send_by_id",  # POST /broadcasts/{id}/send
]

# Generate the mapping dynamically based on the list of operation IDs.
map = { op_id: get_lambda(op_id) for op_id in OPERATION_IDS }
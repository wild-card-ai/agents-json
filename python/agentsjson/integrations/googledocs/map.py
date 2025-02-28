from .tools import Executor
from ..types import ExecutorType

map_type = ExecutorType.SDK

map = {
    "googledocs_create_document": Executor.googledocs_create_document,
    "googledocs_get_document": Executor.googledocs_get_document,
    "googledocs_batch_update_documents": Executor.googledocs_batch_update_documents
}

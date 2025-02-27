from pydantic import BaseModel
from linkup import LinkupClient

class Executor(BaseModel):
    @staticmethod
    def linkup_post_search(api_key: str, **kwargs):
        linkupClient = LinkupClient(api_key=api_key)
        return linkupClient.search(
            query=kwargs.get("q"),
            depth=kwargs.get("depth"),
            output_type="sourcedAnswer"
        )

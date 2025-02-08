from . import resend_client
from typing import Any, Dict
import inspect


def get_positional_args(func):
    sig = inspect.signature(func)
    return [p.name for p in sig.parameters.values() 
            if p.default == inspect.Parameter.empty 
            and p.name not in ('self', 'kwargs')]

class Executor:
    @staticmethod
    def create_client(api_key: str, method_name: str, **kwargs) -> Any:
        """
        Creates and returns a Resend API Client instance based on the method name.

        The method name is used to determine which API client to instantiate.
        For example, a method_name like "resend_get_audiences_by_id" will return an 
        instance of AudiencesApi.

        :param api_key: API key for authentication.
        :param method_name: Name of the method being invoked.
        :return: Instance of the appropriate API client.
        """
        # Mapping between keywords and corresponding API client classes.
        api_mapping = {
            'api_keys': resend_client.APIKeysApi,
            'audiences': resend_client.AudiencesApi,
            'broadcasts': resend_client.BroadcastsApi,
            'contacts': resend_client.ContactsApi,
            'domains': resend_client.DomainsApi,
            'emails': resend_client.EmailsApi,
        }
        
        # Lowercase the method name for case-insensitive matching.
        method_name_lower = method_name.lower()
        selected_client_class = None
        for keyword, client_cls in api_mapping.items():
            if keyword in method_name_lower:
                selected_client_class = client_cls
                break

        # If no matching client is found, default to DefaultApi
        if selected_client_class is None:
            selected_client_class = resend_client.DefaultApi

        configuration = resend_client.Configuration()
        configuration.api_key['api_key'] = api_key
        api_client = resend_client.ApiClient(configuration)
        return selected_client_class(api_client)

    @staticmethod
    def run_method(api_key: str, method_name: str, **kwargs) -> Dict[str, Any]:
        client = Executor.create_client(api_key, method_name, **kwargs)
        method = getattr(client, method_name)
        positional_args = get_positional_args(method)
                
        pos_args_vals = []
        for arg in positional_args:
            if arg == 'api_key':
                pos_args_vals.append(api_key)
            else:
                pos_args_vals.append(kwargs[arg])
                del kwargs[arg]
        
        response = method(*pos_args_vals, **kwargs)
        if hasattr(response, 'to_dict'):
            return response.to_dict()

        return response
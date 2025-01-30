from . import giphy_client
from typing import Any, Dict
import inspect


def get_positional_args(func):
    sig = inspect.signature(func)
    return [p.name for p in sig.parameters.values() 
            if p.default == inspect.Parameter.empty 
            and p.name not in ('self', 'kwargs')]

class Executor:
    @staticmethod
    def create_client(api_key: str, **kwargs) -> giphy_client.DefaultApi:
        """
        Creates and returns a Giphy API Client instance using the provided API key.
        
        Parameters:
            api_key (str): Giphy API Key
        
        Returns:
            giphy_client.DefaultApi: Configured Giphy API Client
        """
        configuration = giphy_client.Configuration()
        configuration.api_key['api_key'] = api_key
        return giphy_client.DefaultApi(giphy_client.ApiClient(configuration))

    @staticmethod
    def run_method(api_key: str, method_name: str, **kwargs) -> Dict[str, Any]:
        client = Executor.create_client(api_key)
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


    

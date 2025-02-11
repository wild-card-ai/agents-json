import re
import sys
from collections.abc import Sized
from benedict import benedict
from typing import Dict, Any, Tuple

def get_deep_size(obj: Any, seen: set = None) -> int:
    """
    Recursively calculate the approximate memory footprint of an object.
    """
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    seen.add(obj_id)
    
    size = sys.getsizeof(obj)
    if isinstance(obj, dict):
        size += sum(get_deep_size(k, seen) + get_deep_size(v, seen) for k, v in obj.items())
    elif isinstance(obj, (list, tuple, set)):
        size += sum(get_deep_size(i, seen) for i in obj)
    return size

def split_responses(execution_data: Dict[str, Any], 
                    threshold: int = 10 * 1024  # Default threshold is 10 KB
                   ) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """
    Splits the responses stored in execution_data into small and large based on a threshold.
    
    Args:
        execution_data: The response data dictionary to be checked.
        threshold: The size threshold in bytes to distinguish between small and large responses.
    
    Returns:
        A tuple containing two dictionaries:
         - The first dictionary contains responses below the threshold.
         - The second dictionary contains responses equal to or above the threshold.
    """
    small_responses = benedict({})
    large_responses = benedict({})

    for key, value in dict(execution_data).items():
        approx_size = get_deep_size(value)
        if approx_size < threshold:
            small_responses[key] = value
        else:
            large_responses[key] = value
            
    return dict(small_responses), dict(large_responses) 

def convert_dot_digits_to_brackets(dot_notation: str) -> str:
    """
    Convert something like "line_items.0.price_data.0" into
    "line_items[0].price_data[0]" so benedict sees array indices.
    """
    return re.sub(r"\.(\d+)(?=\.|$)", r"[\1]", dot_notation)
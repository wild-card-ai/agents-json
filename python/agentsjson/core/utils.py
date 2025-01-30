import re

def convert_dot_digits_to_brackets(dot_notation: str) -> str:
    """
    Convert something like "line_items.0.price_data.0" into
    "line_items[0].price_data[0]" so benedict sees array indices.
    """
    return re.sub(r"\.(\d+)(?=\.|$)", r"[\1]", dot_notation)
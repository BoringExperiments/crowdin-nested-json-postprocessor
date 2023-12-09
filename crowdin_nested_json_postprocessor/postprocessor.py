from typing import Any, Dict


def remove_empty(data: Dict[Any, Any]) -> Dict[Any, Any]:
    """Recursively remove empty items from nested objects (dictionaries and lists)

    ⚙️ Arg:
      data(dict): JSON data

    ↪️ Return:
      str: JSON data without empty keys, list, dict, and array
    """

    if isinstance(data, dict):
        return {
            k: remove_empty(v)
            for k, v in data.items()
            if v is not None and v != "" and remove_empty(v) != {}
        }
    elif isinstance(data, list):
        return [
            remove_empty(v)
            for v in data
            if v is not None and v != "" and remove_empty(v) != []
        ]
    else:
        return data

#"""Format JSON data to be more readable
#
#⚙️ Arg:
#  data(dict): JSON data
#  indent(int): Indentation level
#
#↪️ Return:
#  str: Formatted JSON data with 4 indents
#"""
#
#import json
#
#
#def format_json(
#    data: dict, 
#    indent: int = 2,
#  ) -> dict:
#  """Format JSON data to be more readable
#
#  ⚙️ Arg:
#    data(dict): JSON data
#    indent(int): Indentation level
#
#  ↪️ Return:
#    str: Formatted JSON data with specified indentation
#  """
#
#  return json.dumps(data, indent=indent, ensure_ascii=False)

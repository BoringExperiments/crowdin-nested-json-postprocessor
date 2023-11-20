import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
# import lib.formatter as formatter  # noqa: E402
import lib.cleanup as cleanup      # noqa: E402


class TestLibrary:


  #def test_formatter(self):
  #  """Format JSON data to be more readable
  #  
  #  ⚙️ Expected result:
  #    Formatted JSON data with 2 indents
  #  """
  #  assert (
  #    formatter.format_json({"test": "test"})
  #    == b'{\n  "test": "test"\n}'
  #  )


  def test_remove_empty(self):
    """Recursively remove empty items from nested objects (dictionaries and lists)
    
    ⚙️ Expected result:
      JSON data without empty keys, list, dict, and array
    """

    assert (
      cleanup.remove_empty(
        {
            "htcrehbgfd": {
              "foo": "bar",
              "bar": "it",
              "asdf": "",
              "eat": "sleep",
              "bfdshgrtvcs": "repeat",
            },
            "fceafcds": "",
            "test": "fceayshuicfysdifyicewfiw",
            "feacsfcdsa": {},
            "fcedafxdgera": {
              "xfeasfdasxf": "cfeawfzgfd",
              "gibberish": "aevffadcxs",
              "asdf": "",
            },
        }
      )
        ) == {
            "htcrehbgfd": {
              "foo": "bar",
              "bar": "it",
              "eat": "sleep",
              "bfdshgrtvcs": "repeat",
            },
            "test": "fceayshuicfysdifyicewfiw",
            "fcedafxdgera": {
              "xfeasfdasxf": "cfeawfzgfd", 
              "gibberish": "aevffadcxs"
            },
        }
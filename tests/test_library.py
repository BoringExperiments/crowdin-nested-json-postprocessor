import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
import crowdin_nested_json_postprocessor.postprocessor as postprocessor  # noqa: E402


class TestLibrary:
	def test_remove_empty(self):
		"""Recursively remove empty items from nested objects (dictionaries and lists)

		⚙️ Expected result:
			JSON data without empty keys, list, dict, and array
		"""

		assert (
			postprocessor.remove_empty(
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
			"fcedafxdgera": {"xfeasfdasxf": "cfeawfzgfd", "gibberish": "aevffadcxs"},
		}

# `> Nested JSON Postprocessor`

Remove null or empty keys, list and array from JSON files.

| Python version | Support status   |
| -------------- | ---------------- |
| Upcoming       | ⚙️ Best effort   |
| 3.12           | ✅ Supported     |
| 3.11           | ✅ Supported     |
| 3.10           | ✅ Supported     |
| 3.9            | ✅ Supported     |
| 3.8            | ⚙️ Best effort   |
| 3.7            | ⚙️ Best effort   |
| =<3.6          | ❌ Not Supported |

## `> Postprocessor // Usage`

> [!IMPORTANT]  
> This guide assume that you already installed Python 3.10 or higher

### `> Postprocessor // Preparing the files`

1. Clone the repository: `git@github.com:validcube/crowdin-nested-json-postprocessor.git`
2. Create two new folder called: `input` and `output`
3. Copy the JSON files that you want to process into the `input` folder

### `> Postprocessor // Running the script`

Running the script:

1. Install the required dependencies: `pip3 install -r requirements.txt`
2. Run the script: `python3 main.py`

## `> Postprocessor // Contributing`

Consider checking out the [CONTRIBUTING.md](CONTRIBUTING.md) page.

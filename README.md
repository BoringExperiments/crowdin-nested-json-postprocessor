# GitHub Action `> Nested JSON Postprocessor`

Remove null or empty keys, list and array from JSON files.

## `> Postprocessor // Usage`

Before you start, make sure that you have setup the supported version of Python in your workflow:

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

```yml
- name: Set up Python 3.12
  uses: actions/setup-python@v4
  with:
    python-version: 3.12
```

| Input             | Required                          | Description      |
| ----------------- | --------------------------------- | ---------------- |
| `token`           | ✅ Yes                            | GitHub token     |
| `source_dir`      | ✅ Yes                            | Input directory  |
| `destination_dir` | ❌ No (default to `source_dir`)   | Output directory |
| `signing_key`     | ❌ No                             | Signing key      |
| `commit_message`  | ❌ No (default to `JSON Cleanup`) | Commit message   |

```yml
- name: Nested JSON Postprocessor
  uses: validcube/crowdin-nested-json-postprocessor@v0.1
  with:
    token: ${{ secrets.GITHUB_TOKEN }} # required, your push token
    source_dir: "path/to/your/source/directory" # required, your input directory
    destination_dir: "path/to/your/destination/directory" # optional, default to source_dir
    signing_key: "your-signing-key" # optional, will skip signing if not provided
    commit_message: "your-custom-commit-message" # optional, default to "JSON Cleanup"
```

## `> Postprocessor // Contributing`

Consider checking out the [CONTRIBUTING.md](CONTRIBUTING.md) page.

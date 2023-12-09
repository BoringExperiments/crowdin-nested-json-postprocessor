## `> Nested JSON Postprocessor // Contributing`

Thanks for consider contributing.

### `> Python`

> [!IMPORTANT]  
> This guide assume that you already installed Python 3.10 or higher and pytest.

Developing the script:

1. Install the required dependencies for development: `pip3 install -r dev-requirements.txt`
2. Lint check: `ruff .`
3. Static Analysis: `mypy .`
4. Test the script: `pytest`

> [!WARNING]  
> Ruff is a linter made using Rust, it's super fast and doesn't output anything if everything passes, don't fall for it!

### `> GitHub Action Composite`

When contributing to GitHub Action Composite, please make sure that you follow [security hardening guide](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions).

## `> Nested JSON Postprocessor // Tips`

- All commits must follows the [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) guidelines.
- [Signing commits](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits) are required.
- This repository follows slight variation of [Google's Python style](https://google.github.io/styleguide/pyguide.html) guide **but not strictly enforced**.

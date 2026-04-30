# AI Agent Dev Helper

Small LangChain-based coding helper that can read, write, and list files in a restricted workspace.

## Features

- Builds an agent with a configurable Gemini model.
- Uses tool wrappers for filesystem actions.
- Restricts file access to a configured base directory.
- Loads runtime configuration from `.env`.
- Adds structured logging with redaction/truncation support.

## Project Structure

- `main.py` - entrypoint that builds and invokes the agent.
- `agent/builder.py` - agent construction and tool wiring.
- `config/settings.py` - environment-backed configuration and base path setup.
- `tools/filesystem.py` - file read/write/list tools exposed to the agent.
- `tools/utils.py` - path safety validation helpers.
- `prompts/system.py` - system prompt used by the agent.
- `core/logging.py` - shared logging configuration and decorators.

## Requirements

- Python 3.10+
- A valid Google Generative AI API key

## Setup

1. Create and activate a virtual environment.
2. Install dependencies (example):
   - `pip install langchain langchain-google-genai pydantic-settings`
3. Create `.env` from `.env.example` and set values:
   - `api_key`
   - `app_path`
   - `model`
   - Optional: `LOG_LEVEL` (`DEBUG`, `INFO`, `WARNING`, `ERROR`)

## Run

From the project root:

`python main.py`

## Logging

Logging is configured in `core/logging.py` and is designed to be safer than plain print statements.

- Uses Python `logging` with timestamp/level/module output.
- Supports configurable level via `LOG_LEVEL`.
- Redacts common sensitive keys (`api_key`, `token`, `password`, etc.).
- Truncates large string payloads to reduce log noise.
- Logs exceptions with stack traces for easier debugging.

## Safety Notes

- File tools resolve paths relative to `app_path`.
- Traversal outside `app_path` is blocked by path validation.
- `write_file` can overwrite existing files, so use with care.

## Next Improvements

- Add `pyproject.toml` with pinned dependencies and tooling config.
- Add tests for path safety and tool behavior.
- Add CI for linting and tests.
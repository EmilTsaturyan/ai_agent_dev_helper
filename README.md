# AI Agent Dev Helper

LangChain-based development assistant that generates and iterates on code in a restricted workspace using an orchestrated multi-step flow.

## What It Does

- Uses a Gemini chat model configured from environment variables.
- Runs a pipeline of specialized agents: planner, builder, tester, fixer, and reviewer.
- Exposes filesystem tools for reading, writing, and listing files in a safe base directory.
- Executes `pytest` and retries with automatic fixing when tests fail (up to 3 iterations).
- Adds centralized logging with truncation and sensitive value redaction.

## Runtime Flow

`main.py` creates the LLM agent with tools, then passes it to `Orchestrator`.

`Orchestrator.run(task)` performs:
1. Plan generation.
2. Build/code generation.
3. Test generation.
4. Real `pytest` execution with up to 3 fix loops if failures are detected.
5. Final review and returned state snapshot.

## Project Structure

- `main.py` - entrypoint, tool wiring, and default task prompt.
- `agent/orchestrator.py` - end-to-end workflow coordination.
- `agent/base.py` - base wrapper for role-specific agent calls.
- `agent/planner.py` - planning agent prompt and class.
- `agent/builder.py` - implementation agent prompt and class.
- `agent/tester.py` - test-writing agent prompt and class.
- `agent/fixer.py` - failure-fixing agent prompt and class.
- `agent/reviewer.py` - review agent prompt and class.
- `agent/state.py` - shared state model for orchestration.
- `config/settings.py` - `.env` loading and global `GOOGLE_API_KEY` setup.
- `tools/filesystem.py` - `read_file`, `write_file`, `list_files`, `create_directory` tools.
- `tools/utils.py` - path safety and sandbox validation helpers.
- `prompts/system.py` - system behavior rules used by the tool-enabled agent.
- `core/logging.py` - logger setup and tool-call logging decorator.

## Requirements

- Python 3.10+
- Google Generative AI API key

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Create `.env` from `.env.example`.
4. Configure required variables:
   - `API_KEY`
   - `APP_PATH`
   - `MODEL`
   - Optional: `LOG_LEVEL` (`DEBUG`, `INFO`, `WARNING`, `ERROR`)

## Run

From the project root:

`python main.py`

## Logging

`core/logging.py` configures application-wide logging and tool tracing.

- Configurable level via `LOG_LEVEL`.
- Redacts sensitive keys (for example: `api_key`, `token`, `password`).
- Truncates long string values to reduce noisy logs.
- Logs tool start/completion and stack traces on failure.

## Safety Notes

- All file operations are resolved relative to `APP_PATH`.
- Path traversal outside `APP_PATH` is blocked by safety checks.
- `write_file` overwrites existing files.
- `create_directory` is available in `tools/filesystem.py` (even if not currently passed in `main.py` tool list).

## Notes

- The default task in `main.py` is currently hardcoded; edit the `prompt` variable to run different goals.
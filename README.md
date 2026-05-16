# max-ai

max-ai is a small Python project that combines a Google Gemini AI prompt agent with safe local tooling and a tiny calculator application.

The root app (`main.py`) is designed to accept a plain-language prompt, then use Gemini's function calling to inspect files, read content, write files, or execute Python scripts safely inside a configured working directory.

## What this project includes

- `main.py` - the AI entry point that forwards user prompts to Google Gemini.
- `call_function.py` - bridges Gemini function calls to local Python helpers.
- `functions/` - a set of safe utility operations:
  - `get_files_info` - list directory contents with file size and directory status.
  - `get_file_content` - read a file from the working directory.
  - `write_file` - create/update files inside the working directory.
  - `run_python_file` - execute a Python file with optional CLI arguments.
- `calculator/` - a small calculator app and tests.

![Project Architecture](https://via.placeholder.com/900x320?text=max-ai+Architecture)

## Key features

- AI-driven project exploration using Google Gemini.
- Secure local file operations limited to a permitted working directory.
- A sample calculator app that evaluates simple math expressions and prints JSON output.
- Easy test execution for the calculator component.

## Project structure

- `main.py` - root prompt agent.
- `call_function.py` - tool routing utility.
- `config.py` - project configuration constants.
- `functions/` - function declarations and implementations.
- `calculator/` - calculator app and supporting package.
- `pyproject.toml` - dependency and package metadata.

## Requirements

- Python 3.12 or newer.
- A valid Google Gemini API key.
- Dependencies installed from `pyproject.toml`.

## Setup

1. Create and activate a Python virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` does not exist, use:

   ```bash
   pip install google-genai==1.12.1 python-dotenv==1.1.0
   ```

3. Create a `.env` file in the project root and add your Gemini API key:

   ```ini
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

### Run the AI agent

Use the root `main.py` to ask questions about the project or invoke tooling through the Gemini model.

```bash
python main.py "Read calculator/main.py and explain what it does."
```

Add `--verbose` to show token usage and function-call tracing:

```bash
python main.py "List files in the calculator folder." --verbose
```

### Run the calculator app

The calculator is a standalone sample app:

```bash
python calculator/main.py "3 + 5"
```

Example output:

```json
{
  "expression": "3 + 5",
  "result": 8
}
```

## Running tests

Execute the calculator test suite with Python's `unittest`:

```bash
python -m unittest calculator/tests.py
```

## How the AI tools work

The AI agent uses `google.genai` with explicit function declarations defined in `functions/*.py`.

- `get_files_info` inspects a folder inside the working directory.
- `get_file_content` reads text files safely.
- `write_file` writes files and creates directories as needed.
- `run_python_file` executes Python code inside the allowed workspace.

The agent is instructed to keep operations local to the working directory and to focus on understanding the project.

## Notes

- `run_python_file` uses the `python3` interpreter command, so ensure your environment resolves this command correctly on Windows or adjust as needed.
- The project is intentionally small and easy to extend with new AI-aware tools.
- If you want a real diagram, replace the placeholder image URL with your own file or screenshot.

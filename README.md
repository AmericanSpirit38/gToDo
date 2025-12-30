# gToDo

Basic Python to‑do app.

## Requirements
- Python 3.8+ recommended

## Installation
```bash
# Clone the repository
git clone https://github.com/AmericanSpirit38/gToDo.git
cd gToDo

# (Optional) create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies (if any are listed in requirements.txt)
pip install -r requirements.txt
```

## Usage
Below are common ways to run the app. Update the script name if different (e.g., `app.py`, `main.py`, or `todo.py`).

### Run directly
```bash
python main.py
```

### Add a task (example)
```bash
python main.py add "Buy groceries"
```

### List tasks
```bash
python main.py list
```

### Complete a task
```bash
python main.py done 2
```

### Remove a task
```bash
python main.py remove 3
```

## Development
- Format/linters: (add if used, e.g., `ruff`, `black`, `flake8`)
- Tests: (add command if applicable, e.g., `pytest`)

## Notes
- Tasks storage: (describe, e.g., JSON file `data/tasks.json` in the repo root)
- Config: (mention any config file or env vars if used)

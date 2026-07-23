# NexSpace

## Project Overview

**NexSpace** is a modular command-line interface (CLI) application developed by **NexSemble**. It provides an interactive terminal experience with utilities for generating UUIDs, strong passwords, and managing files - all from a clean `>>>` prompt.

---

## Changes Made & How They Improved the Project

### 1. Moved All Logic Into `NexCLI.py`

**Before:** `main.py` contained business logic mixed with interface code - the CLI loop, file I/O operations, help display, and developer info were all inlined.

**After:** Every function now lives inside the `nexspace` class in `NexCLI.py`. `main.py` is reduced to a pure 3-line interface:

```python
from NexCLI import nexspace

def main():
    Nex = nexspace()
    Nex.start()
```

**Why this is better:**
- **Separation of concerns** - The interface (input/output flow) is fully decoupled from the implementation (what each command does).
- **Maintainability** - To add or modify a command, you only touch `NexCLI.py`. `main.py` never needs to change.
- **Reusability** - The `nexspace` class can be imported and used by any other script or test file.

### 2. Added a Command Dispatch System

**Before:** A long `if/elif` chain lived directly in `main.py`'s while loop.

**After:** Two new methods handle everything:
- `run_command(cmd)` - dispatches a single command and returns `True` to continue or `False` to exit.
- `start()` - the main CLI loop that reads input and feeds it to `run_command()`.

**Why this is better:**
- **Testable** - You can call `Nex.run_command("uuid")` in a unit test without running the full interactive loop.
- **Cleaner exit handling** - `exit` returns `False` instead of calling `sys.exit()`, so the program terminates gracefully.

### 3. Added New File I/O Functions

| Function | Description |
|----------|-------------|
| `newfile(filename)` | Creates a new file safely with error handling |
| `fedit(filename, content)` | Writes content to a file (append mode) |
| `fread(filename)` | Reads and returns file contents |

**Why this is better:**
- **Safe** - Every function validates input and wraps operations in `try/except` so the CLI never crashes on a bad filename.
- **Functional** - `fedit` now actually writes content (the old version just opened the file and did nothing).
- **New capability** - `fread` is a brand-new command that lets users read files without leaving the CLI.

### 4. Added a Help System

**Before:** Users had to memorize commands.

**After:** The `help` command prints a formatted table of all available commands with descriptions, driven by the `COMMANDS` dictionary.

**Why this is better:**
- **Discoverable** - New users can explore available commands immediately.
- **Self-documenting** - The `COMMANDS` dictionary is the single source of truth; adding a command and its description in one place updates the help output automatically.

### 5. Rebranded from NexCLI to NexSpace

**Before:** The project was named NexCLI with a banner reading "NexCLI".

**After:** Everything - the banner ASCII art, welcome message, exit message, class name, and README - now says **NexSpace**.

**Why this is better:**
- **Consistent identity** - The project name is unified across all user-facing surfaces.

### 6. Improved Error Handling & Robustness

- **KeyboardInterrupt handling** - Ctrl+C now exits cleanly with a goodbye message instead of a traceback.
- **Global exception guard** - Unexpected errors print a clean error message and let the loop continue instead of crashing.
- **Input validation** - All file commands check for empty filenames before acting.

### 7. Code Structure Improvements

- **Constants at the top** - `BANNER` and `COMMANDS` are module-level constants.
- **Comments** - Each section is labeled (`display / meta`, `generators`, `file operations`, `command dispatch`).
- **Module docstrings** - Both files have docstrings explaining their purpose.

---

## Getting Started

1. Run the application:
   ```bash
   python main.py
   ```
2. Press **Enter** when prompted to start
3. Type `help` at the `>>>` prompt to see all commands

---

## Project Structure

```
.
├── main.py     # Thin entry point - imports and starts nexspace
├── NexCLI.py   # Core nexspace class with ALL logic & command dispatch
└── README.md   # Project documentation
```

---

## Commands Available

| Command       | Description                              |
|---------------|------------------------------------------|
| `help`        | Show available commands                   |
| `info`        | Show developer & project info             |
| `uuid`        | Generate a random UUID                    |
| `pwd`         | Generate a 12-character strong password   |
| `newfile`     | Create a new file                         |
| `fedit`       | Write content to a file (append mode)      |
| `fread`       | Read content from a file                   |
| `dev_check1`  | Debug - split command into characters      |
| `exit`        | Exit NexSpace                              |

---

## Developer

- **Name**: Atharv Sharma
- **Designation**: Founder of NexSemble
- **Project**: First project under NexSemble, for introducing the community to NexSpace

---

## Requirements

- Python 3.x
- Standard library modules: `uuid`, `random`, `string`, `os`

---



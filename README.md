# EasyLog

**Simple Logging Library for Python**

EasyLog is a lightweight and colorful logging utility for Python. It supports different log levels, module-based tagging (core logs), and writes both to the terminal and to a log file. Perfect for small projects and debugging.

## Features

- ✅ Colored terminal output
- ✅ Log levels: `info`, `warn`, `error`, `success`
- ✅ Core/module-aware log variants
- ✅ Automatic log file writing
- ✅ Thread-safe (with optional locking)

## Installation

Clone this repository and include `logger.py` in your project.

```bash
git clone https://github.com/enversabri/easylog.git
```
## 🚀 Usage


```python
from logger import Logger

Logger.set_file("logs/app.log")

Logger.info("Application started.")
Logger.warn("This is a warning.")
Logger.error("An error occurred.")
Logger.success("Operation completed successfully.")

Logger.coreInfo("Auth", "User login successful.")
Logger.coreError("Database", "Connection failed.")
```
## 🖨️ Output Example

```plaintext
[INFO] Application started.
[WARN] This is a warning.
[ERROR] An error occurred.
[SUCCESS] Operation completed successfully.

[Auth] User login successful.
[Database] Connection failed.
```

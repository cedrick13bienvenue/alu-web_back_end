# Personal data

## Description
This project covers handling Personally Identifiable Information (PII)
safely: obfuscating PII in logs, connecting to a database using credentials
from environment variables, and hashing passwords instead of storing them
in plain text.

## Resources
- [What Is PII, non-PII, and Personal Data?](https://piwik.pro/blog/what-is-pii-personal-data/)
- [logging documentation](https://docs.python.org/3/library/logging.html)
- [bcrypt package](https://pypi.org/project/bcrypt/)
- [Logging to Files, Setting Levels, and Formatting](https://docs.python.org/3/howto/logging.html)

## Learning Objectives
By the end of this project, you should be able to explain, without Google:
- Examples of Personally Identifiable Information (PII)
- How to implement a log filter that obfuscates PII fields
- How to encrypt a password and check the validity of an input password
- How to authenticate to a database using environment variables

## Requirements
- All files interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/env python3`
- Code follows the `pycodestyle` style (version 2.5)
- All files are executable
- All modules, classes, and functions are documented with real, explanatory docstrings
- All functions are type-annotated

## Setup
```
pip3 install -r requirements.txt
```
Tasks 3 and 4 need a MySQL database reachable via `PERSONAL_DATA_DB_USERNAME`,
`PERSONAL_DATA_DB_PASSWORD`, `PERSONAL_DATA_DB_HOST`, and `PERSONAL_DATA_DB_NAME`.

## Tasks
| File | Description |
| --- | --- |
| `filtered_logger.py` | `filter_datum`, `RedactingFormatter`, `get_logger`, `get_db`, and `main` - obfuscated logging and reading PII from a database |
| `encrypt_password.py` | `hash_password` and `is_valid` - bcrypt-based password hashing and validation |

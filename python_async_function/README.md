# Python - Async

## Description
This project covers asynchronous programming in Python 3: the `async`/`await`
syntax, running coroutines concurrently, measuring runtime, and creating
`asyncio` tasks.

## Resources
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Learning Objectives
By the end of this project, you should be able to explain, without Google:
- `async` and `await` syntax
- How to execute an async program with `asyncio`
- How to run concurrent coroutines
- How to create `asyncio` tasks
- How to use the `random` module

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/env python3`
- Code follows the `pycodestyle` style (version 2.5.x)
- All files are executable
- All functions and coroutines are type-annotated
- All modules and functions are documented with real, explanatory docstrings

## Tasks
| File | Description |
| --- | --- |
| `0-basic_async_syntax.py` | Coroutine that waits a random delay and returns it |
| `1-concurrent_coroutines.py` | Runs `wait_random` concurrently `n` times, returns delays in ascending order |
| `2-measure_runtime.py` | Measures the average runtime of `wait_n` |
| `3-tasks.py` | Wraps `wait_random` in an `asyncio.Task` |
| `4-tasks.py` | Same as `wait_n` but built on `asyncio.Task`s |

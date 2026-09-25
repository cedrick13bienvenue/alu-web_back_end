# Python - Async Comprehension

## Description
This project covers asynchronous generators, async comprehensions, and how
to type-annotate generators in Python 3.

## Resources
- [PEP 530 -- Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
- [What's New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#pep-530-asynchronous-comprehensions)
- [Type-hints for generators](https://docs.python.org/3/library/typing.html#typing.Generator)

## Learning Objectives
By the end of this project, you should be able to explain, without Google:
- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/env python3`
- Code follows the `pycodestyle` style (version 2.5.x)
- All functions and coroutines are type-annotated
- All modules and functions are documented with real, explanatory docstrings

## Tasks
| File | Description |
| --- | --- |
| `0-async_generator.py` | Asynchronous generator yielding 10 random numbers, one per second |
| `1-async_comprehension.py` | Collects the generator's values using an async comprehension |
| `2-measure_runtime.py` | Runs 4 async comprehensions in parallel with `asyncio.gather` and times it |

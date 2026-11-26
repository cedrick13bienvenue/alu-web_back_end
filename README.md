# ALU Web Back End

This repository holds my back-end projects for the ALU Software Engineering
program. Each project lives in its own top-level directory with its own
`README.md`, tasks, and (where required) test/main files.

## Projects

| Directory | Project |
| --- | --- |
| [`python_variable_annotations`](./python_variable_annotations) | Python 3 type annotations: function signatures, variable types, duck typing, and validating code with `mypy` |
| [`python_async_function`](./python_async_function) | Asynchronous Python: `async`/`await`, concurrent coroutines, and `asyncio` tasks |
| [`python_async_comprehension`](./python_async_comprehension) | Async generators, async comprehensions, and type-annotating generators |
| [`pagination`](./pagination) | REST API pagination: simple, hypermedia, and deletion-resilient |
| [`personal_data`](./personal_data) | PII-safe logging, database credentials via environment variables, and bcrypt password hashing |
| [`Unittests_and_integration_tests`](./Unittests_and_integration_tests) | Unit and integration testing: mocking, `parameterized`, fixtures, and a full `unittest.mock.patch`-based GithubOrgClient test suite |
| [`i18n`](./i18n) | Flask internationalization with Flask-Babel: locale/timezone selection from URL params, user settings, and request headers |
| [`0x0B_redis_basic`](./0x0B_redis_basic) | A Redis-backed cache with call counting, call history, and replay, via decorators |
| [`MySQL_Advanced`](./MySQL_Advanced) | Constraints, triggers, stored procedures/functions, views, and indexes in MySQL |
| [`NoSQL`](./NoSQL) | MongoDB CRUD via shell scripts and PyMongo, plus an Nginx log stats aggregation |
| [`ES6_basic`](./ES6_basic) | ES6 syntax: const/let, arrow functions, default/rest/spread params, template literals |
| [`ES6_promise`](./ES6_promise) | ES6 Promises: then/catch/finally, Promise.all/allSettled/race, throw/try/catch |
| [`ES6_classes`](./ES6_classes) | ES6 classes: getters/setters, static methods, inheritance, and metaprogramming with symbols |

More projects will be added here as new directories as the program progresses.

## Conventions
- Python files target Python 3.7 on Ubuntu 18.04 LTS, start with `#!/usr/bin/env python3`, follow `pycodestyle`, and are executable.
- SQL files target MySQL 5.7 on Ubuntu 18.04 LTS, start with a comment describing the task, and use uppercase SQL keywords.
- Every module, class, and function is documented with a real docstring.
- Each project directory contains its own `README.md` with task-specific details.

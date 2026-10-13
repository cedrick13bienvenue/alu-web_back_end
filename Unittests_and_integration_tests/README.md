# Unittests and Integration Tests

## Description
This project covers unit testing and integration testing in Python:
mocking, parameterizing tests, and testing an end-to-end code path while
only mocking the low-level calls that cross a process boundary (HTTP, in
this case).

## Resources
- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [How to mock a readonly property with mock?](https://stackoverflow.com/questions/11836436/how-to-mock-a-readonly-property-with-mock)
- [parameterized](https://pypi.org/project/parameterized/)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)

## Learning Objectives
By the end of this project, you should be able to explain, without Google:
- The difference between unit and integration tests
- Common testing patterns such as mocking, parametrizations, and fixtures

## Requirements
- All files interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/env python3`
- Code follows the `pycodestyle` style (version 2.5)
- All files are executable
- All modules, classes, and functions are documented with real, explanatory docstrings
- All functions and coroutines are type-annotated

## Setup
```
pip3 install parameterized
```

## Running the tests
```
python3 -m unittest path/to/test_file.py
```

## Tasks
| File | Description |
| --- | --- |
| `utils.py`, `client.py`, `fixtures.py` | Platform-provided source under test (`access_nested_map`, `get_json`, `memoize`, `GithubOrgClient`) |
| `test_utils.py` | Unit tests for `access_nested_map`, `get_json` (mocked HTTP), and `memoize` |
| `test_client.py` | Unit tests for `GithubOrgClient` (mocked `get_json`/properties) plus an integration test suite for `public_repos`, parameterized from `fixtures.py` |

## A note on `parameterized.expand` / `parameterized_class` and docstrings
Both decorators replace the original method/class name with generated,
per-case copies (e.g. `test_access_nested_map_0`, `TestIntegrationGithubOrgClient_0`).
Introspecting the original pre-decoration name's `__doc__` no longer
reflects the real test — the docstrings live on the generated copies that
actually run. This is expected behavior of the `parameterized` library, not
a bug in these tests.

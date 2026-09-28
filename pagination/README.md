# Pagination

## Description
This project covers pagination techniques for a REST API: paginating with
simple `page`/`page_size` parameters, adding hypermedia metadata to a
paginated response, and paginating in a way that survives deletions from
the underlying dataset.

## Resources
- [REST API Design: Pagination](https://restfulapi.net/pagination/)
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)

## Learning Objectives
By the end of this project, you should be able to explain, without Google:
- How to paginate a dataset with simple `page` and `page_size` parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Requirements
- All files interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/env python3`
- Code follows the `pycodestyle` style (version 2.5.*)
- All modules and functions are documented with real, explanatory docstrings
- All functions and coroutines are type-annotated

## Setup
This project uses `Popular_Baby_Names.csv` as its dataset, placed alongside the task files in this directory.

## Tasks
| File | Description |
| --- | --- |
| `0-simple_helper_function.py` | `index_range` - computes the start/end index for a page |
| `1-simple_pagination.py` | `Server.get_page` - returns a page of rows from the dataset |
| `2-hypermedia_pagination.py` | `Server.get_hyper` - adds pagination metadata (next/prev page, total pages) |
| `3-hypermedia_del_pagination.py` | `Server.get_hyper_index` - pagination that stays consistent even if rows are deleted between requests |

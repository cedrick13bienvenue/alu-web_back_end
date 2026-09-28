#!/usr/bin/env python3
"""Module for computing pagination index ranges."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the start and end index range for a given page and size."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

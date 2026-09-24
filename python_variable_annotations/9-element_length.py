#!/usr/bin/env python3
"""Module for duck-typed function annotations."""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples pairing each element with its length."""
    return [(i, len(i)) for i in lst]

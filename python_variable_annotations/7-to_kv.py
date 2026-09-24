#!/usr/bin/env python3
"""Module for type-annotated key-value tuple operations."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of a string and the square of a number as a float."""
    return (k, v ** 2)

#!/usr/bin/env python3
"""Module for type-annotated higher-order functions."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def multiplier_function(x: float) -> float:
        """Multiply x by the enclosing multiplier."""
        return x * multiplier
    return multiplier_function

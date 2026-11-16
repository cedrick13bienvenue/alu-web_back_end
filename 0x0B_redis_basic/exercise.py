#!/usr/bin/env python3
"""Module that defines a Redis-backed Cache class."""
from typing import Callable, Optional, Union
import uuid
import redis


class Cache:
    """A thin wrapper around Redis for storing and retrieving data."""

    def __init__(self) -> None:
        """Connect to Redis and flush any data from a previous run."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data under a random key and return that key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float, None]:
        """Return the value stored at key, converted by fn if given."""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """Return the value stored at key, decoded as a UTF-8 string."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Return the value stored at key, converted to an integer."""
        return self.get(key, fn=int)

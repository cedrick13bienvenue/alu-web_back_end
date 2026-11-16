#!/usr/bin/env python3
"""Module that defines a Redis-backed Cache class."""
from typing import Union
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

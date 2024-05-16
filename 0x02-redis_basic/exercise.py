#!/usr/bin/env python3
"""strings_to_redis
"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """Implements a Cache using Redis."""

    def __init__(self):
        """create a Redis instance."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key, store input data in Redis using
        the random key.

        :param data: input data to store
        :return: the return the key used to store the input data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable]) -> Union[str, bytes, int, None]:
        """Retrieve a value from Redis using key and convert data back"""
        value = self._redis.get(key)

        if value is None:
            return None
        if fn is None:
            return value
        return fn(value)

    def get_str(self, value: str) -> str:
        """convert data back to string"""
        if type(value) is str:
            return value.decode("utf-8")

    def get_int(self, value: str) -> int:
        """convert data back to number"""
        if type(value) is int or float:
            return int(value)

#!/usr/bin/env python3
"""strings_to_redis
"""
import redis
import uuid
from typing import Union


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

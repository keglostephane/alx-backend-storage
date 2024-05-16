#!/usr/bin/env python3
"""strings_to_redis
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """a decorator that count the number of calls of a method"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """count the number of calls of wrapped function"""
        return self._redis.incr(key)
    return wrapper


def call_history(method: Callable) -> Callable:
    """a decorator that store the history of input/output
    for a function.
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """store the history of input"""
        input_list = "{}:inputs".format(method.__qualname__)
        output_list = "{}:outputs".format(method.__qualname__)

        output = method(self, *args, **kwargs)
        self._redis.rpush(input_list, str(args))
        self._redis.rpush(output_list, output)

        return output

    return wrapper


class Cache:
    """Implements a Cache using Redis."""

    def __init__(self):
        """create a Redis instance."""
        self._redis = redis.Redis()
        self._redis.flushdb()


    @call_history
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
            fn: Optional[Callable] = None) -> Union[str, bytes, int]:
        """Retrieve a value from Redis using key and convert data back"""
        value = self._redis.get(key)
        if not value:
            return value
        return fn(value) if fn is not None else value

    def get_str(self, key: str) -> str:
        """convert data back to string"""
        return self.get(key, fn=lambda s: s.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """convert data back to number"""
        return self.get(key, fn=int)

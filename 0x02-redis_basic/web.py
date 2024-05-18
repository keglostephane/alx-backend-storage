#!/usr/bin/env python3
"""redis_web_cache_tracker
"""
import requests
import redis
from functools import wraps
from typing import Callable


conn = redis.Redis()


def count_calls(func: Callable) -> Callable:
    """a decorator that count the number of call of a function"""
    @wraps(func)
    def wrapper(url):
        """count the numbers of calls"""
        cache_key = f"cache:{url}"
        count_key = f"count:{url}"
        ttl = 10
        cache_value = conn.get(cache_key)

        if cache_value:
            return cache_value.decode('utf-8')

        resp = func(url)
        conn.set(cache_key, resp, ex=ttl)
        conn.incr(count_key)

        return resp

    return wrapper


@count_calls
def get_page(url: str) -> str:
    """get html content from a url"""
    resp = requests.get(url)
    return resp.text


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    get_page(url)

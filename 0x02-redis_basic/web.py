#!/usr/bin/env python3
"""redis_web_cache_tracker
"""
import requests
import redis
from functools import wraps
from typing import Callable


conn = redis.Redis()


def count_call(func: Callable) -> Callable:
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
        conn.incr(count_key)
        conn.set(cache_key, resp, ex=ttl)

        return resp

    return wrapper


@count_call
def get_page(url: str) -> str:
    """get html content from a url"""
    resp = requests.get(url)
    return resp.text


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    count_key = f"count:{url}"

    get_page(url)

    print("{} has been called {} times.".format(
        get_page.__qualname__, conn.get(count_key)
    ))

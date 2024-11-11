#!/usr/bin/env python3
"""
Module to cache webpage content and track access count with Redis.
"""
import requests
import redis
from typing import Callable
from functools import wraps


redis_client = redis.Redis()


def cache_page(func: Callable) -> Callable:
    """Decorator to cache a webpage result and track access count."""
    @wraps(func)
    def wrapper(url: str) -> str:
        count_key = f"count:{url}"
        cache_key = f"cache:{url}"

        redis_client.incr(count_key)

        cached_content = redis_client.get(cache_key)
        if cached_content:
            return cached_content.decode('utf-8')

        content = func(url)
        redis_client.setex(cache_key, 10, content)
        return content

    return wrapper


@cache_page
def get_page(url: str) -> str:
    """Fetches HTML content of a URL and returns it."""
    response = requests.get(url)
    return response.text

#!/usr/bin/env python3
"""
    Module to setup cache with redis
"""
import redis
import uuid
from typing import Union


class Cache:
    """
        Class definition for redis caching
    """

    def __init__(self) -> None:
        """ Initializes the class instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Stores data into redis using random key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

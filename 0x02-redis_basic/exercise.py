#!/usr/bin/env python3
"""
    Module to setup cache with redis
"""
import redis
import uuid
from typing import Any


class Cache:
    """
        Class definition for redis caching
    """

    def __init__(self) -> None:
        """ Initializes the class instance """
        self._redis = redis.Redis()

    def store(self, data: Any) -> str:
        """ Stores data into redis using random key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

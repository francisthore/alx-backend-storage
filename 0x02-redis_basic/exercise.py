#!/usr/bin/env python3
"""
    Module to setup cache with redis
"""
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, int, bytes, None]:
        """Retrieves a value in its form"""
        obj = self._redis.get(key)
        if obj is None:
            return None
        return fn(obj) if fn else obj

    def get_str(self, key: str) -> Optional[str]:
        """Retrieves a sting from redis"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieves an int from redis"""
        return self.get(key, lambda x: int(x))

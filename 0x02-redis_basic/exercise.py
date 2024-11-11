#!/usr/bin/env python3
"""
    Module to setup cache with redis
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator that counts the number of times a method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        key = method.__qualname__
        self._redis.incr(key)

        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store history of inputs and outputs."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper


def replay(method: Callable) -> None:
    """Displays the history of calls for a particular function."""
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    self = method.__self__
    inputs = self._redis.lrange(input_key, 0, -1)
    outputs = self._redis.lrange(output_key, 0, -1)

    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for input_args, output in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{input_args.decode('utf-8')}) -> {output.decode('utf-8')}")


class Cache:
    """
        Class definition for redis caching
    """

    def __init__(self) -> None:
        """ Initializes the class instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

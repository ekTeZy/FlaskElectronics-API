import time
from typing import Any, Optional


class CacheManager:
    _cache = {}

    @classmethod
    def get(cls, key: str) -> Optional[Any]:
        if key in cls._cache and cls._cache[key]["expiration_time"] > time.time():
            return cls._cache[key]["value"]

        return None

    @classmethod
    def set(cls, key: str, value: Any, timeout: int = 300) -> None:
        cls._cache[key] = {
            "value": value,
            "expiration_time": time.time() + timeout
        }

    @classmethod
    def clear(cls) -> None:
        cls._cache.clear()

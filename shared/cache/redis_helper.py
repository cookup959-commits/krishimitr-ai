import os
import json
import logging
from typing import Any, Optional
from dotenv import load_dotenv

load_dotenv()
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

logger = logging.getLogger("cache")

# Fallback in-memory cache
class MemoryCache:
    def __init__(self):
        self._store = {}
        self._expire = {}

    def get(self, key: str) -> Optional[str]:
        import time
        if key in self._store:
            # Check expiration
            expire_at = self._expire.get(key)
            if expire_at and time.time() > expire_at:
                self.delete(key)
                return None
            return self._store[key]
        return None

    def set(self, key: str, value: str, ex: Optional[int] = None) -> bool:
        import time
        self._store[key] = value
        if ex:
            self._expire[key] = time.time() + ex
        else:
            self._expire.pop(key, None)
        return True

    def delete(self, key: str) -> bool:
        self._store.pop(key, None)
        self._expire.pop(key, None)
        return True

# Initialize client
redis_client = None
use_memory_cache = True

try:
    import redis
    redis_client = redis.from_url(REDIS_URL, decode_responses=True)
    # Test connection
    redis_client.ping()
    use_memory_cache = False
    logger.info("Connected to Redis successfully.")
except Exception as e:
    logger.warning(f"Failed to connect to Redis: {e}. Falling back to in-memory cache.")
    redis_client = MemoryCache()

def get_cache(key: str) -> Optional[Any]:
    try:
        val = redis_client.get(key)
        if val:
            return json.loads(val)
    except Exception as e:
        logger.error(f"Error reading from cache: {e}")
    return None

def set_cache(key: str, value: Any, expire_seconds: Optional[int] = 300) -> bool:
    try:
        val_str = json.dumps(value)
        redis_client.set(key, val_str, ex=expire_seconds)
        return True
    except Exception as e:
        logger.error(f"Error writing to cache: {e}")
        return False

def delete_cache(key: str) -> bool:
    try:
        redis_client.delete(key)
        return True
    except Exception as e:
        logger.error(f"Error deleting from cache: {e}")
        return False

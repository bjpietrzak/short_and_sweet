from redis import Redis
from fastapi import HTTPException
from typing import Tuple

from setup import REDIS, ERRORS


class RedisClient:
    def __init__(self, redis_db: Redis) -> None:
        self.redis = redis_db

    def clear_all(self):
        self.redis.flushdb()

    def cache(self, key: str, value: list | dict | str) -> None:
        self.redis.delete(key)
        if value is None or not value:
            pass
        elif isinstance(value, dict):
            for k, v in value.items():
                self.redis.hset(key, k, v)
        elif isinstance(value, str):
            self.redis.set(key, value)
        elif isinstance(value, list):
            self.redis.rpush(key, *value)

    def get_cache(self, key: str) -> list | dict | str:
        if not self.redis.exists(key):
            raise KeyError(f"Key '{key}' does not exist in cache.")
        data_type = self.redis.type(key)
        if data_type == 'list':
            return self.redis.lrange(key, 0, -1)
        elif data_type == 'hash':
            return self.redis.hgetall(key)
        elif data_type == 'string':
            return self.redis.get(key)
        else:
            return None

    def ready(self) -> bool:
        return self.redis.exists(*REDIS['dependencies']) == \
                                 len(REDIS['dependencies'])

    def ping(self) -> bool:
        return self.redis.ping()
    
    def get_more_data(self) -> Tuple[list, list, list,
                                     list, list, list]:
        if not self.ready():
            raise HTTPException(status_code=400,
                                detail=ERRORS['resultsNotReady'])
        else:
            return (self.get_cache(key) for key in REDIS['dependencies'])


redis_db = Redis(
    host=REDIS['setup']['host'],
    port=REDIS['setup']['port'],
    encoding="utf-8",
    decode_responses=True)
redis_client = RedisClient(redis_db)
redis_client.ping()
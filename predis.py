import redis
import settings


class predis():
    def __init__(self):
        self._r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

    def rpush(self, code):
        self._r.rpush('codes', code)
        return True

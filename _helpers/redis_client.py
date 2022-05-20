from redis import StrictRedis
from pdfbaz.settings.base import REDIS_HOST, REDIS_PORT


class RedisClient:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RedisClient, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self):
        if not hasattr(self, 'client'):
            self.client = StrictRedis(host=REDIS_HOST,
                                      port=REDIS_PORT,
                                      db=0)

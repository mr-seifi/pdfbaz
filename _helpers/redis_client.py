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


# PREFIX
BOOK_PREFIX = 'b'

# EXPIRATIONS
BOOK_TTL = 3600 * 24

REDIS_KEYS = {
    'book_exist': f'{BOOK_PREFIX}'':{book_id}',
    'book_url': f'{BOOK_PREFIX}'':{book_id}:url',
    'hash_to_id': f'{BOOK_PREFIX}'':{book_hash}:hash',
}

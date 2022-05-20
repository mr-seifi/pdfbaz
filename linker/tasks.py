from payment.models import OrderBook
from store.models import Book
from _helpers.redis_client import RedisClient, BOOK_TTL
from django.contrib.auth.models import User
from _helpers.redis_client import REDIS_KEYS
from uuid import uuid4


def _is_exist(book: Book) -> bool:
    client = RedisClient().client
    result = client.get(REDIS_KEYS.get('book_exist').format(book_id=book.id))

    return (True, False)[not result]


def _get_url(book: Book) -> str:
    client = RedisClient().client
    result = client.get(REDIS_KEYS.get('book_url').format(book_id=book.id))

    return result.decode()


def _make_available(book: Book) -> int:
    client = RedisClient().client
    result = client.set(name=REDIS_KEYS.get('book_exist').format(book_id=book.id),
                        value=1,
                        ex=BOOK_TTL)

    return 1


def _generate_download_url(book: Book) -> str:
    client = RedisClient().client
    uuid = uuid4().hex
    result = client.set(name=REDIS_KEYS.get('book_url').format(book_id=book.id),
                        value=uuid,
                        ex=BOOK_TTL)

    return uuid


def generate_download_url(book: Book):
    if _is_exist(book):
        return _get_url(book)

    _make_available(book)
    return _generate_download_url(book)

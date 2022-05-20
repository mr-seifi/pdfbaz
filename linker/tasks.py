from payment.models import OrderBook
from store.models import Book
from _helpers.redis_client import RedisClient, BOOK_TTL
from django.contrib.auth.models import User
from _helpers.redis_client import REDIS_KEYS
from uuid import uuid4
from provider.tasks import download_book


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
    client.set(name=REDIS_KEYS.get('book_exist').format(book_id=book.id),
               value=1,
               ex=BOOK_TTL)

    return 1


def _generate_download_url(book: Book) -> str:

    download_book(book)
    client = RedisClient().client
    uuid = uuid4().hex
    client.set(name=REDIS_KEYS.get('book_url').format(book_id=book.id),
               value=uuid,
               ex=BOOK_TTL)
    client.set(name=REDIS_KEYS.get('hash_to_id').format(book_hash=uuid),
               value=book.id,
               ex=BOOK_TTL)

    return uuid


def get_book_id(book_hash: str) -> int:
    client = RedisClient().client
    result = client.get(name=REDIS_KEYS.get('hash_to_id').format(book_hash=book_hash))

    return result.decode()


def generate_download_url(book: Book = False, book_hash=None):
    if book_hash:
        book = Book.objects.get(pk=get_book_id(book_hash))

    if _is_exist(book):
        return _get_url(book)

    _make_available(book)
    return _generate_download_url(book)

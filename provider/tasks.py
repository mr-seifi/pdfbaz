import requests
from store.models import Book
from django.core.files.base import ContentFile


def _download_book(book: Book):

    with requests.Session() as session:
        content = ContentFile(session.get(book.download_url).content)
        book.file.save(name=f'{book.slug}.{book.download_url.split(".")[-1]}', content=content, save=True)

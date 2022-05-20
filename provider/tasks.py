import requests
from store.models import Book
from django.core.files.base import ContentFile
from store.services.libgen_service import LibgenService


def download_book(book: Book):

    with requests.Session() as session:
        content = ContentFile(session.get(book.download_url.replace('31.42.184.140', '62.182.86.140')).content)
        filename = f'{LibgenService.get_book_identifier(book.__dict__)}.{book.extension}'
        book.file.save(name=filename, content=content, save=True)

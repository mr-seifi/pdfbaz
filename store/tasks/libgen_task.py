from store.models import Book, Author, Publisher
from store.services.libgen_service import LibgenService
from multiprocessing.pool import Pool


def _add_book(book: dict):
    libgen_service = LibgenService()

    try:
        print('[+] Process started!')
        authors = libgen_service.split_authors(authors=book['authors'])
        authors = [Author.objects.get_or_create(name=author) for author in authors]
        authors = list(map(lambda x: x[0], authors))

        print('[+] Author added!')
        publisher, _ = Publisher.objects.get_or_create(name=book['publisher'])
        print('[+] Publisher added!')

        book = Book.objects.create(libgen_id=book['id'],
                                   title=book['title'],
                                   series=book['series'],
                                   year=book['year'],
                                   edition=book['edition'],
                                   publisher=publisher,
                                   pages=book['pages'],
                                   language='en',
                                   filesize=book['filesize'],
                                   extension=book['extension'],
                                   topic=book['topic'],
                                   identifier=book['identifier'],
                                   md5=book['md5'],
                                   description=book.get('description', ''),
                                   download_url=book.get('link', ''),
                                   cover_url=LibgenService.get_cover_url(book))
        print(f'[+] Book {book.id} created!')

        [book.authors.add(author) for author in authors]
        print('[+] Authors added!')

    except Exception as ex:
        print(f'[-] {ex}')


def add_books_to_database():
    libgen_service = LibgenService()

    for batch in libgen_service.read_book_from_mysql(limit=5000):
        print('[+] Assign process started!')
        libgen_service.assign_more_information(batch)
        print('[+] Assigned successfully!')

        with Pool() as pool:
            pool.starmap(_add_book, [(book, ) for book in batch])


# TODO: Each time update offset by last added book libgen_id in database (Make this automated)

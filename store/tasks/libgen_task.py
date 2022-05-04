from store.models import Book, Author, Publisher
from store.services.libgen_service import LibgenService
from multiprocessing.pool import Pool


def _add_book(book: dict):
    libgen_service = LibgenService()

    try:
        if Book.objects.filter(libgen_id=book['id']):
            print(f'[-] Passed: {book["id"]}')
            return

        authors_name = libgen_service.split_authors(authors=book['authors'])
        authors = [Author.objects.get_or_create(name=author) for author in authors_name]
        authors = list(map(lambda x: x[0], authors))
        publisher, _ = Publisher.objects.get_or_create(name=book['publisher'])

        book = Book(libgen_id=book['id'],
                    title=book['title'],
                    series=book['series'],
                    year=book['year'],
                    edition=book['edition'],
                    publisher=publisher,
                    pages=book['pages'] or None,
                    language=book['language'],
                    filesize=book['filesize'],
                    extension=book['extension'],
                    topic=book['topic'] or 'Other',
                    identifier=book['identifier'],
                    md5=book['md5'],
                    description=book.get('description', ''),
                    download_url=book.get('link', ''),
                    cover_url=LibgenService.get_cover_url(book))
        book.save(publisher=publisher.name, authors=", ".join(authors_name))
        print(f'[+] Book {book.id} created!')

        [book.authors.add(author) for author in authors]

    except Exception as ex:
        print(f'[-] {ex}, data: {book}')


def add_books_to_database_online(limit=5000, offset=0):
    libgen_service = LibgenService()

    for batch in libgen_service.read_book_from_mysql(limit=limit, offset=offset):
        print('[+] Assign process started!')
        libgen_service.assign_more_information_online(batch)
        print('[+] Assigned successfully!')

        with Pool() as pool:
            pool.starmap(_add_book, [(book,) for book in batch])


def add_books_to_database(limit=5000, offset=0):
    libgen_service = LibgenService()

    for batch in libgen_service.read_book_from_mysql(limit=limit, offset=offset):
        with Pool() as pool:
            pool.starmap(_add_book, [(book,) for book in batch])
        # for book in batch:
        #     _add_book(book)
        print('[+] Batch looped!')

# TODO: Each time update offset by last added book libgen_id in database (Make this automated)

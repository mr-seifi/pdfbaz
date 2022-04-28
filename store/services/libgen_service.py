import re
from bs4 import BeautifulSoup
import requests
from mysql.connector import connect
from concurrent.futures import ThreadPoolExecutor
from threading import Lock


class LibgenService:
    _instance = None
    assigned_cnt = 0

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance') or not getattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'conn') or not getattr(self, 'conn'):
            from secret import MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, MYSQL_HOST
            self.conn = connect(user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB, host=MYSQL_HOST)

    def read_book_from_mysql(self, limit=100000, offset=0):
        cursor = self.conn.cursor()
        select_query = 'SELECT * FROM updated u ' \
                       'LEFT JOIN topics t ON u.topic = t.topic_id ' \
                       'WHERE u.Language = "English" AND (t.lang = "en" OR t.lang IS NULL)' \
                       ' LIMIT {limit} OFFSET {offset}'
        cursor.execute(select_query.format(limit=limit, offset=offset))
        data = cursor.fetchall()

        while data:
            offset += limit
            yield LibgenService._libgen_record_to_dict(data=data)
            cursor.execute(select_query.format(limit=limit, offset=offset))
            data = cursor.fetchall()

    @staticmethod
    def get_cover_url(book: dict):
        return f"http://library.lol/covers/{book.get('cover_url', '')}" if book.get('cover_url') else ''

    @staticmethod
    def split_authors(authors: str) -> list:
        return [author.strip() for author in authors.split(',') if author]

    @staticmethod
    def assign_more_information(book_list: list):
        with ThreadPoolExecutor() as executor:
            with requests.Session() as session:
                executor.map(LibgenService._assign_more_information, book_list, [session] * len(book_list))
                executor.shutdown()

    @staticmethod
    def _assign_more_information(book: dict, session: requests.Session):
        description = LibgenService._get_description_online(book=book,
                                                            session=session)
        link = LibgenService._get_book_link_online(book=book,
                                                   session=session)
        if description:
            book['description'] = description
        if link:
            book['link'] = link

        LibgenService.assigned_cnt += 1
        print(f'\r[+] Assigning progress: {LibgenService.assigned_cnt}', end='')
        return book

    @staticmethod
    def _get_description_online(book: dict, session: requests.Session):
        base_url = 'http://library.lol/main/'

        if not book.get("md5"):
            return

        url = f'{base_url}{book.get("md5")}'
        response = session.get(url)

        if response.status_code != 200:
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        if result := re.findall(r'<div>Description:<br\/>(.+)<\/div>', str(soup)):
            return result[0]

    @staticmethod
    def _get_book_link_online(book: dict, session: requests.Session):
        base_url = 'http://library.lol/main/'

        if not book.get("md5"):
            return

        url = f'{base_url}{book.get("md5")}'
        response = session.get(url)

        if response.status_code != 200:
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        if result := re.findall(r'<a href="(.+)">GET<\/a>', str(soup)):
            return result

    @staticmethod
    def _libgen_record_to_dict(data):
        return list(map(lambda book: {'id': book[0],
                                      'title': book[1],
                                      'series': book[3],
                                      'authors': book[5],
                                      'year': book[6],
                                      'edition': book[7],
                                      'publisher': book[8],
                                      'pages': book[10],
                                      'pages_in_file': book[11],
                                      'language': book[12],
                                      'identifier': book[16],
                                      'issn': book[17],
                                      'asin': book[18],
                                      'udc': book[19],
                                      'lbc': book[20],
                                      'ddc': book[21],
                                      'lcc': book[22],
                                      'doi': book[23],
                                      'openlibrary_id': book[24],
                                      'filesize': book[35],
                                      'extension': book[36],
                                      'md5': book[37],
                                      'cover_url': book[44],
                                      'topic': book[48]}, data))

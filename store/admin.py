from django.contrib import admin
from store.models import Author, Publisher, Book

admin.register([Author, Publisher, Book])
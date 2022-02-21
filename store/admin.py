from django.contrib import admin
from .models import Author, Publisher, Book

admin.site.register([Author, Publisher, Book])

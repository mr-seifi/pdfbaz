from django.contrib import admin

from .models import Author, Publisher, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created',)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created', )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'cover', 'filesize', 'extension', )
    list_filter = ('topic', 'year', 'language', 'extension', )
    search_fields = ('title', 'author', 'publisher', )

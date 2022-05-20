from django.contrib import admin
from .models import OrderBook


@admin.register(OrderBook)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_token', 'customer', 'book', )
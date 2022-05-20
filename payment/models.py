from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from store.models import Book


class OrderBook(models.Model):
    order_id = models.UUIDField(default=uuid4)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['order_id']),
            models.Index(fields=['customer', 'book']),
        ]

    @classmethod
    def has_payment(cls, user: User, book: Book):
        orders = cls.objects.filter(customer=user,
                                    book=book)

        return (True, False)[not orders]

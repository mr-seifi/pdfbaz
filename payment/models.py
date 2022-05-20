from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from store.models import Book


class OrderBook(models.Model):
    order_token = models.UUIDField(default=uuid4)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['order_token']),
            models.Index(fields=['customer', 'book']),
        ]

    @classmethod
    def has_payment(cls, user: User, book: Book):
        orders = cls.objects.filter(customer_id=user.id,
                                    book=book)

        return (True, False)[not orders]

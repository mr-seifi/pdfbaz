# Generated by Django 4.0.2 on 2022-05-04 10:28

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_book_document'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='book',
            index=django.contrib.postgres.indexes.GinIndex(fields=['document'], name='store_book_documen_844838_gin'),
        ),
    ]

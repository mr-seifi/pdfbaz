# Generated by Django 4.0.2 on 2022-05-20 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_book_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
    ]

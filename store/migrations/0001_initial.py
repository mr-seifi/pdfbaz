# Generated by Django 4.0.2 on 2022-05-04 10:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libgen_id', models.IntegerField(default=-1, unique=True)),
                ('title', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=5000)),
                ('description', models.TextField(blank=True, null=True)),
                ('series', models.TextField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1800), django.core.validators.MaxValueValidator(2100)])),
                ('edition', models.TextField(blank=True)),
                ('pages', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('language', models.CharField(choices=[('English', 'en'), ('Russian', 'ru'), ('French', 'fr'), ('Spanish', 'es'), ('German', 'de'), ('Italian', 'it')], default='English', max_length=50)),
                ('topic', models.TextField(default='Other')),
                ('cover_url', models.URLField(blank=True, max_length=2000, null=True)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='covers')),
                ('identifier', models.TextField(blank=True)),
                ('md5', models.CharField(blank=True, max_length=300)),
                ('filesize', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('extension', models.CharField(choices=[('pdf', 'PDF'), ('epub', 'EPUB'), ('djvu', 'DJVU'), ('doc', 'DOC'), ('mobi', 'MOBI'), ('rar', 'RAR'), ('zip', 'ZIP'), ('azw3', 'AZW3')], default='pdf', max_length=50)),
                ('download_url', models.URLField(blank=True, max_length=2000, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('price', models.IntegerField(default=149000)),
                ('discount', models.IntegerField(default=15)),
                ('publisher_name', models.TextField(blank=True, null=True)),
                ('authors_name', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='publisher',
            index=models.Index(fields=['name'], name='store_publi_name_92bbd8_idx'),
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='published_books', to='store.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='published_books', to='store.publisher'),
        ),
        migrations.AddIndex(
            model_name='author',
            index=models.Index(fields=['name'], name='store_autho_name_28e2a0_idx'),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['libgen_id'], name='store_book_libgen__611373_idx'),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['title'], name='store_book_title_579c41_idx'),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['slug'], name='store_book_slug_22f0c8_idx'),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['identifier'], name='store_book_identif_b665cb_idx'),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['authors_name'], name='store_book_authors_854676_idx'),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['publisher_name'], name='store_book_publish_eb2cfa_idx'),
        ),
    ]

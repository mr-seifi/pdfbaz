# Generated by Django 4.0.2 on 2022-05-20 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='orderbook',
            name='payment_ord_order_i_c504ce_idx',
        ),
        migrations.RemoveIndex(
            model_name='orderbook',
            name='payment_ord_custome_63e52c_idx',
        ),
        migrations.RenameField(
            model_name='orderbook',
            old_name='order_id',
            new_name='order_token',
        ),
        migrations.AddIndex(
            model_name='orderbook',
            index=models.Index(fields=['order_token'], name='payment_ord_order_t_ce04cd_idx'),
        ),
        migrations.AddIndex(
            model_name='orderbook',
            index=models.Index(fields=['customer', 'book'], name='payment_ord_custome_63d8b7_idx'),
        ),
    ]

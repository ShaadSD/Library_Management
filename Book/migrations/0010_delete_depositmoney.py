# Generated by Django 5.0.6 on 2024-10-26 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0009_book_quantity_alter_book_borrowing_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DepositMoney',
        ),
    ]

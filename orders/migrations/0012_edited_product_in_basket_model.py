# Generated by Django 5.0.6 on 2024-06-12 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_created_product_in_basket_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinbasket',
            name='unit_price',
        ),
    ]
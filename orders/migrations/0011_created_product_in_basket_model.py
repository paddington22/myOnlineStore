# Generated by Django 5.0.6 on 2024-06-12 09:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_created_shopping_basket_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.shoppingbasket', verbose_name='Корзина')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.product', verbose_name='Товар')),
            ],
        ),
        migrations.AddField(
            model_name='shoppingbasket',
            name='orders',
            field=models.ManyToManyField(through='orders.ProductInBasket', to='orders.product'),
        ),
    ]

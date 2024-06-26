# Generated by Django 5.0.6 on 2024-06-12 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_edited_baskets_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingbasket',
            name='orders',
            field=models.ManyToManyField(blank=True, null=True, through='orders.ProductInBasket', to='orders.product'),
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='№ заказа')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.product', verbose_name='Товар')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='orders',
            field=models.ManyToManyField(through='orders.ProductInOrder', to='orders.product'),
        ),
    ]

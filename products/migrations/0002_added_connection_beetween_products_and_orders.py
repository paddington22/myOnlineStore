# Generated by Django 5.0.6 on 2024-06-16 22:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_reorganized_project'),
        ('products', '0001_reorganized_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinorder',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='№ заказа'),
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-23 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restro_app', '0005_order_order_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.JSONField(),
        ),
    ]

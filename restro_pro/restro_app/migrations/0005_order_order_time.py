# Generated by Django 5.0.3 on 2024-03-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restro_app', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
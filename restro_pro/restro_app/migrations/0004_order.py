# Generated by Django 5.0.3 on 2024-03-23 07:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restro_app', '0003_remove_cart_qty'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=1000)),
                ('total_price', models.IntegerField()),
                ('order_status', models.CharField(max_length=20)),
                ('amount_status', models.CharField(max_length=20)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restro_app.cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
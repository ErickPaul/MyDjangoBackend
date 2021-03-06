# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-06 09:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecentlyViewedProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='product_name',
            field=models.TextField(null=True),
        ),
    ]

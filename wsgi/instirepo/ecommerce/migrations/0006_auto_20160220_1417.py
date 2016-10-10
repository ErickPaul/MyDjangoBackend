# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_auto_20160207_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bill_availabe',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='warranty_left',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='recentlyviewedproducts',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
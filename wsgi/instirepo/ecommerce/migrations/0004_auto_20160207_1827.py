# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-07 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_auto_20160207_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentlyviewedproducts',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
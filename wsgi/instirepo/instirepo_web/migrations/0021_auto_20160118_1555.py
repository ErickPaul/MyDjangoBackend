# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-18 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instirepo_web', '0020_eventdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdetails',
            name='registration_fee',
            field=models.TextField(blank=True, null=True),
        ),
    ]

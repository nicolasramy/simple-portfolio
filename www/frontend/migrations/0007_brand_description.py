# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_auto_20170601_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

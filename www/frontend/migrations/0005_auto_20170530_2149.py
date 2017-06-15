# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 21:49
from __future__ import unicode_literals

from django.db import migrations, models
import frontend.models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_auto_20170529_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('value', models.TextField()),
            ],
            options={
                'verbose_name': 'parameter',
                'verbose_name_plural': 'parameters',
            },
        ),
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to=frontend.models.get_upload_to_path),
        ),
    ]

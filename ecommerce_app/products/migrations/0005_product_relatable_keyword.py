# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20170804_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='relatable_keyword',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Keyword to relate'),
        ),
    ]

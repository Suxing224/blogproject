# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-07-07 03:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190707_1137'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '标签', 'verbose_name_plural': '标签'},
        ),
    ]
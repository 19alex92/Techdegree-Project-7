# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-03-21 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20190320_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
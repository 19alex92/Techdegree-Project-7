# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-03-19 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190319_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(auto_now=True),
        ),
    ]

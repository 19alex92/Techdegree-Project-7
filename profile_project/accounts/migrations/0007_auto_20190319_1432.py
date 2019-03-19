# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-03-19 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190319_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorite_animal',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='favorite_food',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='profile',
            name='hobby',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
    ]
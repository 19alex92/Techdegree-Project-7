# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-03-21 16:01
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_profile_editor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='editor',
            field=tinymce.models.HTMLField(),
        ),
    ]
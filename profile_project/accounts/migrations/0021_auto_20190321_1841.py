# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-03-21 17:41
from __future__ import unicode_literals

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_profile_editor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='editor',
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=froala_editor.fields.FroalaField(blank=True, default=''),
        ),
    ]

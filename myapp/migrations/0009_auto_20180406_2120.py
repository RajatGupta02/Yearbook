# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-06 15:50
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20180406_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='votes',
            field=jsonfield.fields.JSONField(),
        ),
    ]

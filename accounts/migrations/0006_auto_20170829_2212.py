# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-29 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20170829_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='designation',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

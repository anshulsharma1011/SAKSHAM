# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-30 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saksham2017', '0003_trialsapplications'),
    ]

    operations = [
        migrations.AddField(
            model_name='trialsapplications',
            name='fullname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='trialsapplications',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-30 12:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('saksham2017', '0006_trialsapplications_branch'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='trialsapplications',
            unique_together=set([('user', 'sports_name')]),
        ),
    ]

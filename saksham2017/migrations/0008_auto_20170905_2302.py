# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-05 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saksham2017', '0007_auto_20170830_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='addsport',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addteams',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='addsport',
            name='sports_name',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='addteams',
            name='team_name',
            field=models.CharField(choices=[('Computer Science and Engineering', 'Computer Science and Engineering'), ('Information Technology', 'Information Technology'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Electricals Engineering', 'Electricals Engineering'), ('Electronics and Instrumentation', 'Electronics and Instrumentation'), ('MBA', 'MBA'), ('MCA', 'MCA')], default='', max_length=100, unique=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-28 14:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(default='', max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='', max_length=10)),
                ('branch', models.CharField(choices=[('CSE', 'Computer Science and Engineering'), ('IT', 'Information Technology'), ('ECE', 'Electronics and Communication Engineering'), ('ME', 'Mechanical Engineering'), ('CE', 'Civil Engineering'), ('EN', 'Electricals Engineering'), ('EI', 'Electronics and Instrumentation'), ('MBA', 'MBA'), ('MCA', 'MCA')], default='CSE', max_length=250)),
                ('session', models.CharField(default='', max_length=20)),
                ('contact_details', models.CharField(default='', max_length=15)),
                ('accommodation', models.CharField(choices=[('Hosteler', 'Hosteler'), ('Day Scholar', 'Day Scholar')], default='', max_length=20)),
                ('profile_photo', models.FileField(null=True, upload_to='')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

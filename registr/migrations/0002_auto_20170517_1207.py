# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-17 12:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registr', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersession',
            old_name='user',
            new_name='username',
        ),
        migrations.AddField(
            model_name='usersession',
            name='key',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='usersession',
            name='value',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.RemoveField(
            model_name='usersession',
            name='session',
        ),
        migrations.AlterUniqueTogether(
            name='usersession',
            unique_together=set([('username', 'key')]),
        ),
    ]

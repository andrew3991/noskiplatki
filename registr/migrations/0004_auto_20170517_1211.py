# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-17 12:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registr', '0003_auto_20170517_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=30)),
                ('key', models.CharField(blank=True, max_length=30)),
                ('value', models.CharField(blank=True, max_length=30, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='usersession',
            unique_together=set([('username', 'key')]),
        ),
    ]
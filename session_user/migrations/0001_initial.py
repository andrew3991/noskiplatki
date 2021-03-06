# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-17 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('key', models.CharField(max_length=30)),
                ('value', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='account_data',
            unique_together=set([('username', 'key')]),
        ),
    ]

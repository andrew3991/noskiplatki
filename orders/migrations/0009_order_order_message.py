# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-24 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_order_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_message',
            field=models.TextField(blank=True),
        ),
    ]

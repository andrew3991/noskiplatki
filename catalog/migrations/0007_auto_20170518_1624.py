# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-18 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20170518_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.IntegerField(choices=[(1, '35-38'), (2, '39-42'), (3, '43-45')], default=0, verbose_name='Размер'),
        ),
    ]

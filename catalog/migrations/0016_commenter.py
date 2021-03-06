# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-22 17:19
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0015_auto_20170624_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('content', models.TextField(verbose_name='Комментарий')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата комментария')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='catalog.Product', verbose_name='Product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]

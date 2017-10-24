# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_article_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='content',
        ),
        migrations.AddField(
            model_name='article',
            name='editormd',
            field=models.TextField(default='', verbose_name='editormd'),
            preserve_default=False,
        ),
    ]

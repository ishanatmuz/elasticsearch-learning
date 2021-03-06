# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 03:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elasticsearchapp', '0004_blogpost_metadata'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(max_length=10240)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elasticsearchapp.Blog')),
            ],
        ),
    ]

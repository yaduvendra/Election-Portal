# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-07 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Election_Portal', '0004_remove_candidate_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='id',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='user',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
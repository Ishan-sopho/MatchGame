# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20170904_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='lastanswered',
            field=models.IntegerField(default=1),
        ),
    ]

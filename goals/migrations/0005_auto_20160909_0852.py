# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 08:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0004_auto_20160909_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goals', to=settings.AUTH_USER_MODEL),
        ),
    ]
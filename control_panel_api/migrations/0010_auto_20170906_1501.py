# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 15:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel_api', '0009_auto_20170905_1004'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AppS3BucketAccess',
            new_name='AppS3Bucket',
        ),
    ]

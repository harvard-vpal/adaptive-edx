# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 16:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lti', '0002_ltiparameters_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ltiparameters',
            old_name='timestamp',
            new_name='timestamp_last_launch',
        ),
    ]

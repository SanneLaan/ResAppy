# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 20:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_recipe_ingredient_1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='time',
            new_name='time_in_minutes',
        ),
    ]
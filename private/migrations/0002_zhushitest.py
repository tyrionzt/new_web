# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-07-17 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('private', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZhushiTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='\u54c8\u54c8', max_length=10)),
                ('password', models.CharField(help_text='\u563f\u563f', max_length=100)),
            ],
        ),
    ]

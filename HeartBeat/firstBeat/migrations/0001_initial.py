# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-24 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.CharField(max_length=500)),
                ('opA', models.CharField(max_length=200)),
                ('opB', models.CharField(max_length=200)),
                ('opC', models.CharField(max_length=200)),
                ('opD', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
            ],
        ),
    ]

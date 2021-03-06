# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-02 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_administrator_photo2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjectName', models.CharField(max_length=250)),
                ('Description', models.CharField(max_length=500)),
                ('PlayStoreLink', models.CharField(max_length=250)),
                ('Technology', models.CharField(max_length=250)),
                ('Photo', models.ImageField(default=0, max_length=50, upload_to='MediaAdministrator')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 18:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.CharField(max_length=30)),
                ('valor', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='data',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Type'),
        ),
    ]

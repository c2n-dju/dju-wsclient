# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-19 18:45
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WSCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_update', models.DateTimeField(default=0)),
                ('last_update', models.DateTimeField(default=0)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='WSService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=63)),
                ('portail_name', models.CharField(max_length=63, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WSSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(choices=[('WSS', 'WS'), ('WOSS', 'WOS'), ('RHS', 'RH')], max_length=15, unique=True)),
                ('sitename', models.CharField(max_length=63)),
            ],
        ),
        migrations.AddField(
            model_name='wsservice',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dju_wsclient.WSSite'),
        ),
        migrations.AddField(
            model_name='wscache',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dju_wsclient.WSService'),
        ),
        migrations.AlterUniqueTogether(
            name='wsservice',
            unique_together=set([('site', 'service')]),
        ),
    ]

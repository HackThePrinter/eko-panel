# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 23:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.BigIntegerField()),
                ('description', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='EventSubtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esubtype', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etype', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('nickname', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='esubtype_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ScoreboardEKO13.EventSubtype'),
        ),
        migrations.AddField(
            model_name='event',
            name='etype_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ScoreboardEKO13.EventType'),
        ),
        migrations.AddField(
            model_name='event',
            name='name_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScoreboardEKO13.Name'),
        ),
    ]

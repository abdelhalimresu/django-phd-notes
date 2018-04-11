# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-11 01:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_note_reference'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='note.Note')),
            ],
            options={
                'ordering': ['created_at', 'updated_at'],
            },
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 14:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u79f0')),
                ('href', models.URLField(verbose_name='\u5730\u5740')),
                ('order_index', models.IntegerField(default=99, verbose_name='\u6392\u5e8f')),
                ('status', models.BooleanField(default=True, verbose_name='\u72b6\u6001')),
                ('contact_info', models.CharField(blank=True, max_length=100, verbose_name='\u8054\u7cfb\u65b9\u5f0f')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u6dfb\u52a0\u4eba')),
            ],
            options={
                'verbose_name': '\u53cb\u60c5\u94fe\u63a5',
                'verbose_name_plural': '\u53cb\u60c5\u94fe\u63a5',
            },
        ),
    ]

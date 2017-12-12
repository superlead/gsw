# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 14:36
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
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u540d\u79f0')),
                ('cover_img', models.ImageField(default='uploads/category_default.png', upload_to='uploads/%Y_%m/', verbose_name='\u5c01\u9762\u56fe')),
                ('seo_title', models.CharField(max_length=50, verbose_name='SEO\u6807\u9898')),
                ('seo_keywords', models.CharField(max_length=50, verbose_name='SEO\u5173\u952e\u8bcd')),
                ('seo_desc', models.CharField(max_length=200, verbose_name='SEO\u63cf\u8ff0')),
                ('view_nums', models.IntegerField(default=0, verbose_name='\u9605\u8bfb\u91cf')),
                ('status', models.BooleanField(default=True, verbose_name='\u72b6\u6001')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u521b\u5efa\u4eba')),
            ],
            options={
                'verbose_name': '\u5206\u7c7b\u7ba1\u7406',
                'verbose_name_plural': '\u5206\u7c7b\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='\u6b63\u6587')),
                ('view_nums', models.IntegerField(default=0, verbose_name='\u9605\u8bfb\u91cf')),
                ('dig_nums', models.IntegerField(default=0, verbose_name='\u559c\u6b22\u6570')),
                ('status', models.BooleanField(default=True, verbose_name='\u72b6\u6001')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.Categories', verbose_name='\u5206\u7c7b')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u521b\u5efa\u4eba')),
            ],
            options={
                'verbose_name': '\u53e5\u5b50\u7ba1\u7406',
                'verbose_name_plural': '\u53e5\u5b50\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Speakers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u8a00\u8005')),
                ('intro', models.TextField(verbose_name='\u4ecb\u7ecd')),
                ('cover_img', models.ImageField(default='uploads/speaker_default.png', upload_to='uploads/%Y_%m/', verbose_name='\u5c01\u9762\u56fe')),
                ('seo_title', models.CharField(max_length=50, verbose_name='SEO\u6807\u9898')),
                ('seo_keywords', models.CharField(max_length=50, verbose_name='SEO\u5173\u952e\u8bcd')),
                ('seo_desc', models.CharField(max_length=200, verbose_name='SEO\u63cf\u8ff0')),
                ('view_nums', models.IntegerField(default=0, verbose_name='\u9605\u8bfb\u91cf')),
                ('status', models.BooleanField(default=True, verbose_name='\u72b6\u6001')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u6dfb\u52a0\u4eba')),
            ],
            options={
                'verbose_name': '\u8a00\u8005\u7ba1\u7406',
                'verbose_name_plural': '\u8a00\u8005\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u8bdd\u9898')),
                ('intro', models.TextField(verbose_name='\u4ecb\u7ecd')),
                ('birth_year', models.CharField(max_length=10, verbose_name='\u51fa\u751f\u5e74\u6708')),
                ('cover_img', models.ImageField(default='uploads/topic_default.png', upload_to='uploads/%Y_%m/', verbose_name='\u5c01\u9762\u56fe')),
                ('seo_title', models.CharField(max_length=50, verbose_name='SEO\u6807\u9898')),
                ('seo_keywords', models.CharField(max_length=50, verbose_name='SEO\u5173\u952e\u8bcd')),
                ('seo_desc', models.CharField(max_length=200, verbose_name='SEO\u63cf\u8ff0')),
                ('view_nums', models.IntegerField(default=0, verbose_name='\u9605\u8bfb\u91cf')),
                ('status', models.BooleanField(default=True, verbose_name='\u72b6\u6001')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u6dfb\u52a0\u4eba')),
            ],
            options={
                'verbose_name': '\u8bdd\u9898\u7ba1\u7406',
                'verbose_name_plural': '\u8bdd\u9898\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u4f5c\u54c1\u540d')),
                ('intro', models.TextField(verbose_name='\u4ecb\u7ecd')),
                ('cover_img', models.ImageField(default='uploads/work_default.png', upload_to='uploads/%Y_%m/', verbose_name='\u5c01\u9762\u56fe')),
                ('seo_title', models.CharField(max_length=50, verbose_name='SEO\u6807\u9898')),
                ('seo_keywords', models.CharField(max_length=50, verbose_name='SEO\u5173\u952e\u8bcd')),
                ('seo_desc', models.CharField(max_length=200, verbose_name='SEO\u63cf\u8ff0')),
                ('view_nums', models.IntegerField(default=0, verbose_name='\u9605\u8bfb\u91cf')),
                ('status', models.BooleanField(default=True, verbose_name='\u72b6\u6001')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u6dfb\u52a0\u4eba')),
            ],
            options={
                'verbose_name': '\u4f5c\u54c1\u7ba1\u7406',
                'verbose_name_plural': '\u4f5c\u54c1\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Writers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u4f5c\u8005\u540d')),
                ('intro', models.TextField(verbose_name='\u4ecb\u7ecd')),
                ('birth_year', models.CharField(max_length=10, verbose_name='\u51fa\u751f\u5e74\u6708')),
                ('cover_img', models.ImageField(default='uploads/writer_default.png', upload_to='uploads/%Y_%m/', verbose_name='\u5c01\u9762\u56fe')),
                ('seo_title', models.CharField(max_length=50, verbose_name='SEO\u6807\u9898')),
                ('seo_keywords', models.CharField(max_length=50, verbose_name='SEO\u5173\u952e\u8bcd')),
                ('seo_desc', models.CharField(max_length=200, verbose_name='SEO\u63cf\u8ff0')),
                ('view_nums', models.IntegerField(default=0, verbose_name='\u9605\u8bfb\u91cf')),
                ('status', models.BooleanField(default=True, verbose_name='\u72b6\u6001')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u6dfb\u52a0\u4eba')),
            ],
            options={
                'verbose_name': '\u4f5c\u8005\u7ba1\u7406',
                'verbose_name_plural': '\u4f5c\u8005\u7ba1\u7406',
            },
        ),
        migrations.AddField(
            model_name='works',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.Writers', verbose_name='\u4f5c\u8005'),
        ),
        migrations.AddField(
            model_name='quotes',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.Speakers', verbose_name='\u8a00\u8005'),
        ),
        migrations.AddField(
            model_name='quotes',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.Works', verbose_name='\u4f5c\u54c1'),
        ),
    ]
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.admin import User


class Quotes(models.Model):
    owner = models.ForeignKey(User, verbose_name=u'创建人')
    category = models.ForeignKey('Categories', verbose_name=u'分类')
    speaker = models.ForeignKey('Speakers', verbose_name=u'言者')
    work = models.ForeignKey('Works', verbose_name=u'作品')
    body = models.TextField(verbose_name=u'正文')
    view_nums = models.IntegerField(default=0, verbose_name=u'阅读量')
    dig_nums = models.IntegerField(default=0, verbose_name=u'喜欢数')
    status = models.BooleanField(default=True, verbose_name=u'状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    def __unicode__(self):
        return self.body

    class Meta:
        verbose_name_plural = verbose_name = u'句子管理'


class Categories(models.Model):
    owner = models.ForeignKey(User, verbose_name=u'创建人')
    name = models.CharField(max_length=30, verbose_name=u'名称')
    cover_img = models.ImageField(max_length=100, upload_to='uploads/%Y_%m/', default='uploads/category_default.png', verbose_name=u'封面图')
    seo_title = models.CharField(max_length=50, verbose_name=u'SEO标题')
    seo_keywords = models.CharField(max_length=50, verbose_name=u'SEO关键词')
    seo_desc = models.CharField(max_length=200, verbose_name=u'SEO描述')
    view_nums = models.IntegerField(default=0, verbose_name=u'阅读量')
    status = models.BooleanField(default=True, verbose_name=u'状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = u'分类管理'


class Speakers(models.Model):
    owner = models.ForeignKey(User, verbose_name=u'添加人')
    name = models.CharField(max_length=50, verbose_name=u'言者')
    intro = models.TextField(verbose_name=u'介绍')
    cover_img = models.ImageField(max_length=100, upload_to='uploads/%Y_%m/', default='uploads/speaker_default.png', verbose_name=u'封面图')
    seo_title = models.CharField(max_length=50, verbose_name=u'SEO标题')
    seo_keywords = models.CharField(max_length=50, verbose_name=u'SEO关键词')
    seo_desc = models.CharField(max_length=200, verbose_name=u'SEO描述')
    view_nums = models.IntegerField(default=0, verbose_name=u'阅读量')
    status = models.BooleanField(default=True, verbose_name=u'状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = u'言者管理'


class Works(models.Model):
    owner = models.ForeignKey(User, verbose_name=u'添加人')
    name = models.CharField(max_length=50, verbose_name=u'作品名')
    writer = models.ForeignKey('Writers', verbose_name=u'作者')
    intro = models.TextField(verbose_name=u'介绍')
    cover_img = models.ImageField(max_length=100, upload_to='uploads/%Y_%m/', default='uploads/work_default.png', verbose_name=u'封面图')
    seo_title = models.CharField(max_length=50, verbose_name=u'SEO标题')
    seo_keywords = models.CharField(max_length=50, verbose_name=u'SEO关键词')
    seo_desc = models.CharField(max_length=200, verbose_name=u'SEO描述')
    view_nums = models.IntegerField(default=0, verbose_name=u'阅读量')
    status = models.BooleanField(default=True, verbose_name=u'状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = u'作品管理'


class Writers(models.Model):
    owner = models.ForeignKey(User, verbose_name=u'添加人')
    name = models.CharField(max_length=50, verbose_name=u'作者名')
    intro = models.TextField(verbose_name=u'介绍')
    birth_year = models.CharField(max_length=10, verbose_name=u'出生年月')
    cover_img = models.ImageField(max_length=100, upload_to='uploads/%Y_%m/', default='uploads/writer_default.png', verbose_name=u'封面图')
    seo_title = models.CharField(max_length=50, verbose_name=u'SEO标题')
    seo_keywords = models.CharField(max_length=50, verbose_name=u'SEO关键词')
    seo_desc = models.CharField(max_length=200, verbose_name=u'SEO描述')
    view_nums = models.IntegerField(default=0, verbose_name=u'阅读量')
    status = models.BooleanField(default=True, verbose_name=u'状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = u'作者管理'


class Topics(models.Model):
    owner = models.ForeignKey(User, verbose_name=u'添加人')
    name = models.CharField(max_length=50, verbose_name=u'话题')
    intro = models.TextField(verbose_name=u'介绍')
    birth_year = models.CharField(max_length=10, verbose_name=u'出生年月')
    cover_img = models.ImageField(max_length=100, upload_to='uploads/%Y_%m/', default='uploads/topic_default.png', verbose_name=u'封面图')
    seo_title = models.CharField(max_length=50, verbose_name=u'SEO标题')
    seo_keywords = models.CharField(max_length=50, verbose_name=u'SEO关键词')
    seo_desc = models.CharField(max_length=200, verbose_name=u'SEO描述')
    view_nums = models.IntegerField(default=0, verbose_name=u'阅读量')
    status = models.BooleanField(default=True, verbose_name=u'状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = u'话题管理'





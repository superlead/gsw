# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class FriendLinks(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'名称')
    href = models.URLField(verbose_name=u'地址')
    order_index = models.IntegerField(default=99, verbose_name=u'排序')
    status = models.BooleanField(default=True, verbose_name=u'状态')
    contact_info = models.CharField(max_length=100, blank=True, verbose_name=u'联系方式')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')
    owner = models.ForeignKey(User, verbose_name=u'添加人')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = verbose_name = u'友情链接'
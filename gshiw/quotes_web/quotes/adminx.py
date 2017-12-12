# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from quotes_web.adminx import BaseAdmin
import xadmin
from .models import Quotes, Categories, Works, Writers, Speakers, Topics


class QuotesAdmin(BaseAdmin):
    exclude = ('owner', 'view_nums', 'dig_nums')

xadmin.site.register(Quotes, QuotesAdmin)


class CategoryAdmin(BaseAdmin):
    exclude = ('owner', 'view_nums')
xadmin.site.register(Categories, CategoryAdmin)


class WorkAdmin(BaseAdmin):
    exclude = ('owner', 'view_nums')
xadmin.site.register(Works, WorkAdmin)


class WriterAdmin(BaseAdmin):
    exclude = ('owner', 'view_nums')
xadmin.site.register(Writers, WriterAdmin)


class SpeakerAdmin(BaseAdmin):
    exclude = ('owner', 'view_nums')
xadmin.site.register(Speakers, SpeakerAdmin)


class TopicAdmin(BaseAdmin):
    exclude = ('owner', 'view_nums')
xadmin.site.register(Topics, TopicAdmin)

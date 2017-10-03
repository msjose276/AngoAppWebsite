# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from OurWork.models import *

# Register your models here.
class WorkAdmin(admin.ModelAdmin):
    ordering=['ProjectName']
    list_display=['ProjectName','Description','PlayStoreLink','Technology','Photo']
        
admin.site.register(Work,WorkAdmin)
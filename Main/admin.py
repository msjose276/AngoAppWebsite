# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Main.models import *
from models import *

# Register your models here.

class AdministratorAdmin(admin.ModelAdmin):
    ordering=['Name']
    list_display=['Name','Email','Position','Photo','Photo2']
        
class ClientAdmin(admin.ModelAdmin):
    ordering =['Name']
    list_display=['Name','Email','ProjectName']
    
class WorkAdmin(admin.ModelAdmin):
    ordering=['ProjectName']
    list_display=['ProjectName','Description','PlayStoreLink','Technology','Photo','ReleaseData']
    
    


class UpcomingAdmin(admin.ModelAdmin):
    ordering=['Name']
    list_display=['Name','Photo']
    
admin.site.register(Upcoming,UpcomingAdmin)

admin.site.register(Work,WorkAdmin)

admin.site.register(Administrator,AdministratorAdmin)
admin.site.register(Client,ClientAdmin)
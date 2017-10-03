# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.




class Work(models.Model):
    
    ProjectName=models.CharField(max_length=250)
    Description=models.CharField(max_length=500)
    PlayStoreLink=models.CharField(max_length=250)
    Technology=models.CharField(max_length=250)
    Photo=models.ImageField(upload_to='MediaAdministrator',max_length=50,default=0)

    def __str__(self):
        return self.ProjectName

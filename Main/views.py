# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, Http404
from Main.models import *

# Create your views here.

def HomePage(request):
    #return HttpResponse('<h1>Hello World</h1>')
    All_Upcoming=Upcoming.objects.all()
    return render(request,'homepage.html',{'All_Upcoming':All_Upcoming})
    #All_Administrators=Administrator.objects.all()
    #return render(request,'homepage.html',{'All_Upcoming':All_Administrators})

def AboutUs(request):
    All_Administrators=Administrator.objects.all()
    #return HttpResponse('<h1>Hello World</h1>')
    return render(request,'about.html',{'administrators':All_Administrators})

def portofolio(request):
    All_Work=Work.objects.all()
    return render(request,'portofolio.html',{'All_Work':All_Work})

def process(request):
    All_Administrators=Administrator.objects.all()
    return render(request,'process.html',{})

def services(request):
    All_Administrators=Administrator.objects.all()
    return render(request,'services.html',{})


def contact(request):
    All_Administrators=Administrator.objects.all()
    return render(request,'contact.html',{})
    

def AdministratorView(request,Administrator_name):
    try:
        adminObject=Administrator.objects.get(Name=Administrator_name)
    except Administrator.DoesNotExist:
        raise Http404('it does not exist')
    return render (request, 'SingleWorker.html', {
        'single_worker':adminObject,
        'Photo':adminObject.Photo.url,
        'Name': adminObject.Name,
        'Email': adminObject.Email,
        })


def ClientsView(request,Client_name):
    
    try:
        ClientOject=Client.objects.get(Name=Client_name)
    except Client.DoesNotExist:
        raise Http404('it does not exist')
    return render (request,'SingleWorker.html',{'single_worker':ClientOject})
    #return render (request,'SingleWorker.html',{'single_worker':ClientObject})    
    
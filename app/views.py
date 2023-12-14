from django.shortcuts import render
from app.models import *
from django.http import HttpResponse


def display_topics(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render (request,'display_topics.html',d)


def display_webpages(request):
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    return render (request,'display_webpages.html',d)



def display_accessrecords(request):
    QLAO=AccessRecords.objects.all()
    d={'accessrecords':QLAO}
    return render (request,'display_accessrecords.html',d)



# Create your views here.

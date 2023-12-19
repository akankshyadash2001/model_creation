from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length


def display_topics(request):
    QLTO=Topic.objects.all()
    QLTO=Topic.objects.all().order_by('topic_name')
    QLTO=Topic.objects.all().order_by('-topic_name')
    QLTO=Topic.objects.all().order_by(Length('topic_name'))
    QLTO=Topic.objects.all().order_by(Length('topic_name').desc())
    d={'topics':QLTO}
    return render (request,'display_topics.html',d)


def display_webpages(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.all().order_by('name')
    QLWO=Webpage.objects.all().order_by('-name')
    QLWO=Webpage.objects.all().order_by(Length('name'))
    QLWO=Webpage.objects.all().order_by(Length('name').desc())


    d={'webpages':QLWO}
    return render (request,'display_webpages.html',d)



def display_accessrecords(request):
    QLAO=AccessRecords.objects.all()
    QLAO=AccessRecords.objects.all().order_by('author')
    QLAO=AccessRecords.objects.all().order_by('-author')
    QLAO=AccessRecords.objects.all().order_by(Length('author'))
    QLAO=AccessRecords.objects.all().order_by(Length('author').desc())
    d={'accessrecords':QLAO}
    return render (request,'display_accessrecords.html',d)



# Create your views here.

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

    QLTO=Topic.objects.all().filter(topic_name__gt='A')
    QLTO=Topic.objects.all().filter(topic_name__lt='a')
    QLTO=Topic.objects.all().filter(topic_name__gte='A')
    QLTO=Topic.objects.all().filter(topic_name__lte='a')


    d={'topics':QLTO}
    return render (request,'display_topics.html',d)


def display_webpages(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.all().order_by('name')
    QLWO=Webpage.objects.all().order_by('-name')
    QLWO=Webpage.objects.all().order_by(Length('name'))
    QLWO=Webpage.objects.all().order_by(Length('name').desc())

    QLWO=Webpage.objects.all().filter(name__startswith='M')
    QLWO=Webpage.objects.all().filter(name__endswith='N')
    QLWO=Webpage.objects.all().filter(name__contains='N')

    QLWO=Webpage.objects.all().filter(url__startswith='h')
    QLWO=Webpage.objects.all().filter(url__contains='in')

    


    d={'webpages':QLWO}
    return render (request,'display_webpages.html',d)



def display_accessrecords(request):
    QLAO=AccessRecords.objects.all()
    QLAO=AccessRecords.objects.all().order_by('author')
    QLAO=AccessRecords.objects.all().order_by('-author')
    QLAO=AccessRecords.objects.all().order_by(Length('author'))
    QLAO=AccessRecords.objects.all().order_by(Length('author').desc())

    QLAO=AccessRecords.objects.all().filter(date__year='2001')
    QLAO=AccessRecords.objects.all().filter(date__month='03')
    QLAO=AccessRecords.objects.all().filter(date__day='20')



    d={'accessrecords':QLAO}
    return render (request,'display_accessrecords.html',d)



# Create your views here.

from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

def display_topics(request):
    QST=Topic.objects.all()
    QST=Topic.objects.filter(topic_name='Cricket')
    d={'topics':QST}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(topic_name='Cricket')
    QSW=Webpage.objects.exclude(topic_name='Cricket')
    QSW=Webpage.objects.all()[:5:]
    QSW=Webpage.objects.all().order_by('name')
    QSW=Webpage.objects.order_by('-name')
    QSW=Webpage.objects.filter(topic_name='kabaddi').order_by('-name')
    QSW=Webpage.objects.all().order_by(Length('name'))
    QSW=Webpage.objects.all().order_by(Length('name').desc())
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(url__startswith='https')
    QSW=Webpage.objects.filter(url__endswith='com')
    QSW=Webpage.objects.filter(name__startswith='D')
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(name__contains='d')
    QSW=Webpage.objects.filter(name__regex='\w{7}')
    QSW=Webpage.objects.filter(name__in=['chanukya','sai','nawaaz'])
    QSW=Webpage.objects.filter(Q(topic_name='Cricket')|Q(name='sai'))
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(Q(topic_name='Rugby')&Q(url__startswith='https'))
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)

def display_access(request):
    QSA=AccessRecords.objects.all().order_by('date')
    QSA=AccessRecords.objects.filter(date='2022-12-13')
    QSA=AccessRecords.objects.filter(date__gt='2022-12-13')
    QSA=AccessRecords.objects.filter(date__lte='2022-12-13')
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.filter(date__year='2018')
    QSA=AccessRecords.objects.filter(date__month='8')
    QSA=AccessRecords.objects.filter(date__day='12')
    QSA=AccessRecords.objects.filter(date__year__gt='2018')
    
    d={'access':QSA}
    return render(request,'display_access.html',d)
from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def insert_topic(request):
    tn=input('enter your topic')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('topic is created')


def insert_Webpage(request):
    tn=input('enter your topic')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('ener your name')
    u=input('enter url')

    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('webpage is created')


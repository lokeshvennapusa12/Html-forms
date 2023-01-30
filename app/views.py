from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

#Topic

def insert_topic(request):
    if request.method=='POST':
        #tn=request.POST['topic']
        tn=request.POST.get('topic')
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('Topic is inseted successfully')

    return render(request,'insert_topic.html')

def display_topic(request):
    QST=Topic.objects.all()
    d={ 'topic' : QST }
    return render(request,'display_topic.html',d)

#webpage

def insert_webpage(request):
    topics=Topic.objects.all()
    d={'topics':topics}

    if request.method=='POST':
        tn=request.POST['topic']
        na=request.POST['na']
        date=request.POST['da']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=na,date=date)[0]
        W.save()
        return HttpResponse('Webpage is inserted successfully')
    return render(request,'insert_webpage.html')

def display_webpage(request):
    QSW=Webpage.objects.all()
    d={'webpage': QSW }
    return render(request,'display_webpage.html',d)

#Access_records

def insert_accessrecords(request):
    topics=Topic.objects.all()
    access=Webpage.objects.all()
   
    if request.method=='POST':
        name=request.POST['access']
        date=request.POST['da']
        age=request.POST['age']
        T=Topic.objects.get_or_create(topic_name=topics)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=name,date=date)[0]
        W.save()
        A=Access_records.objects.get_or_create(name=access,age=age)[0]
        A.save()
        
        return HttpResponse('Access_records is inserted successfully')
    return render(request,'insert_accessrecords.html')

  



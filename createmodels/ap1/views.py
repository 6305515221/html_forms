from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from ap1.models import *
from ap1.views import *

def insert_topic(request):
    tn=input("enter the data")
    tod=Topic.objects.get_or_create(topic_name=tn)

    if(tod[1]):
        LTO=Topic.objects.all()
        d={'LTO':LTO}
        return render(request,'display_topic.html',d)
    else:
        return HttpResponse("topic already is created")
    
def insert_webpage(request):
    tn=input("enter the data")
    name=input("enter the name")
    url=input("enter the urls")
    LTO=Topic.objects.filter(topic_name=tn)

    if(LTO):
        wto=Webpages.objects.get_or_create(topic_name=LTO[0],name=name,url=url)
        if(wto[1]):
            LWO=Webpages.objects.all()
            d={"LWO":LWO}
            return render(request,'display_web.html',d)
        else:
            return HttpResponse("web is alredy created")
    else:
        return HttpResponse("parent data is not present")
    
def insert_acees(request):
    id=int(input("enter the id")) ##here name is not primary key becase name contains duplictes so we take id
    author=input("enter the author name")
    date=input("enter the date")
    Lco=Webpages.objects.filter(id=id)
    if(Lco):
        aco=AcessRecords.objects.get_or_create(name=Lco[0],author=author,date=date)
        if(aco[1]):
            LAO=AcessRecords.objects.all()
            d={"LAO":LAO}
            return render(request,'display_acess.html',d)
        else:
            return HttpResponse("acess is already present")
    else:
        return HttpResponse("data is not present in parent ")
    

def display_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    LWO=Webpages.objects.all()
    d={"LWO":LWO}
    return render(request,'display_web.html',d)
def display_acess(request):
    LAO=AcessRecords.objects.all()
    d={"LAO":LAO}
    return render(request,'display_acess.html',d)
# def front_topic1(request):
#     return render(request,'insert_topic.html')

def front_topic(request):
    if request.method=='POST':
        topic_name=request.POST["topic_name"]
        TO=Topic.objects.get_or_create(topic_name=topic_name)
        if(TO):
            return HttpResponse("object is created")
        else:
            return HttpResponse("Data already created")
    else:
        return render(request, 'insert_topic.html')  
    
def front_webpage(request):
    LTO=Topic.objects.all()
    d={"LTO":LTO}
    if request.method=='POST':
        topic_name=request.POST["topic_name"]
        name=request.POST["name"]
        url=request.POST["url"]
        TO=Topic.objects.get(topic_name=topic_name)
        WEB=Webpages.objects.get_or_create(topic_name=TO,name=name,url=url)
        if(WEB):
            return HttpResponse("data is created")
        else:
            return HttpResponse("data is already created")
    else:
        return render(request,'insert_web.html',d)
    
def front_acess(request):
    LTO=Webpages.objects.all()
    d={"LTO":LTO}
    if request.method=='POST':
        name=request.POST['name']
        author=request.POST['author']
        date=request.POST['date']
        TO=Webpages.objects.get(name=name)
        ACO=AcessRecords.objects.get_or_create(name=TO,author=author,date=date)
        if(ACO):
            return HttpResponse("data is created")
        else:
            return HttpResponse("data is already created")
    else:
        return render(request,'insert_acess.html',d)
    
def select_multiple(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        ltns=request.POST.getlist('tns')##['cricket','volley']
        # ltns=request.POST['tns']
        WEQS=Webpages.objects.none()
        for tn in ltns:
            WEQS=WEQS|Webpages.objects.filter(topic_name=tn)
        d1={'WEQS':WEQS}
        return render(request,'display_multiple.html',d1)
    return render(request,'select_multiple.html',d)

def checkbox_view(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'checkbox.html',d)


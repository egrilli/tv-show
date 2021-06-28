from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
from app_tv.models import *
from django.contrib import messages


def index(request):
    return redirect("/shows")


def show(request):
    context={
        "shows":Show.objects.all()
    }
    return render(request,"read-all.html",context)

    
def new(request):
    return render(request,"create.html")

def create(request):

    errors= Show.objects.basic_validator(request.POST)

    if len(errors)>0:
        for k, v in errors.items():
            messages.error(request,v)
        
        request.session['show_title']=request.POST['title']
        request.session['show_network']=request.POST['network']
        request.session['show_release_date']=request.POST['release_date']
        request.session['show_description']=request.POST['description']
        
        return redirect("/shows/new")

    else:
        request.session['show_title']=""
        request.session['show_network']=""
        request.session['show_release_date']=""
        request.session['show_description']=""

    new_show=Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date'],
        description=request.POST['description'],
    )
    return redirect ("/shows/"+str(new_show.id))

def read(request,id):
    show=Show.objects.get(id=id)
    context={
        "show":show
    }
    return render(request,"read.html",context)

def edit(request,id):
    show=Show.objects.get(id=id)
    if request.method=="GET":
        context={
            "show":show
        }
        return render(request,"edit.html",context)

    if request.method=="POST":
        show.title=request.POST['title']
        show.network=request.POST['network']
        show.release_date=request.POST['release_date']
        show.description=request.POST['description']
        show.save()
        return redirect("/shows/"+str(show.id))



def delete(request,id):
    borrar=Show.objects.get(id=id)
    borrar.delete()
    return redirect ("/shows")



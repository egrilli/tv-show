from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
from app_tv.models import *


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



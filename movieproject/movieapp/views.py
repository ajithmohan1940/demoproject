from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from movieapp.models import movie
from .forms import MovieForm


def index(request):
    obj1=movie.objects.all()
    context={"keymovie":obj1}
    return render(request,"index.html",context)
def details(request,mid):
    mov=movie.objects.get(id=mid)
    return render(request,'details.html',{"mov":mov})
def add(request):
    if request.method=="POST":
        name = request.POST.get("name", )
        desc = request.POST.get("description", )
        year = request.POST.get("year", )
        img = request.FILES['img']
        k=movie(name=name,desc=desc,year=year,img=img)
        k.save()

    return render(request,'add.html')
def update(request,id):
    mv=movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=mv)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':mv})

def delete(request,id):
    if request.method=="POST":
        mv=movie.objects.get(id=id)
        mv.delete()
        return redirect('/')
    return render(request,"delete.html")


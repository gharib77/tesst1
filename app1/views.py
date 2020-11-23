from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Personne
from app1.forms import FormPers

# Create your views here.
def index(request):
    personnes= Personne.objects.all()
    return render(request,'app1/first.html',{"personnes":personnes,'wnom':'hhhhhh'})

def add_pers(request):
    if request.method == "POST":
        form= FormPers(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form= FormPers()
    return render(request,'app1/add_pers.html',{'form':form})

def edit_pers(request,id):
    personne= get_object_or_404(Personne,id=id)
    if request.method=="POST":
        form =FormPers(request.POST,instance=personne)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:    
        form = FormPers(instance=personne)
    return render(request,'app1/edit_pers.html',{'form':form})
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Personne
from app1.forms import FormPers



# Create your views here.
def index(request):
    print("jouami",request.user.id)
    personnes= Personne.objects.filter(user_id=request.user.id)
    return render(request,'app1/first.html',{"personnes":personnes,'wnom':'hhhhhh'})

def add_pers(request):
    if request.method == "POST":
        form= FormPers(request.POST)
        if form.is_valid():
            #form.save()
            fs= form.save(commit=False)
            fs.user = request.user
            fs.save()
            
            return redirect('/index')

    else:
        form= FormPers()
    return render(request,'app1/add_pers.html',{'form':form})

def edit_pers(request,id):
    personne= get_object_or_404(Personne,id=id)
    if request.method=="POST":
        form =FormPers(request.POST,instance=personne)
        if form.is_valid():
            form.save()
            return redirect('/index')
    else:    
        form = FormPers(instance=personne)
    return render(request,'app1/edit_pers.html',{'form':form})
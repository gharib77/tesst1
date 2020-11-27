from django.shortcuts import render,redirect
from django.http import HttpResponse
from utilisateurs.forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('/')

def login_view(request):
    form = LoginForm(request.POST,None)
    if form.is_valid():
        username=request.POST['username']
        pwd=request.POST['password']
        user=authenticate(request,username=username,password=pwd)
        if user is  None:
            print("nonnnne")
            messages.error(request,"erurururur")
            return render(request,'utilisateurs/login.html',{"form":form})
        else:
            login(request, user)
            return redirect('/index')
    return render(request,'utilisateurs/login.html',{"form":form})

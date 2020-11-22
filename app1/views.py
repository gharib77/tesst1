from django.shortcuts import render
from django.http import HttpResponse
from .models import Personne

# Create your views here.
def index(request):
    personnes= Personne.objects.all()
    return render(request,'app1/first.html',{"personnes":personnes})
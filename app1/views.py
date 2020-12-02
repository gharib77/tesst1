from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Personne,Ecrivain,Book
from app1.forms import FormPers,FormEcr,FormBook
from django.forms import modelformset_factory,inlineformset_factory
from django.db import transaction, IntegrityError
from datetime import datetime
import calendar




# Create your views here.
def list_ecr(request):
    ecrivains = Ecrivain.objects.all()
    context={'ecrivains':ecrivains}
    return render(request,'app1/list_ecr.html',context)

def editecr(request,id):
    frmbook = inlineformset_factory(Ecrivain, Book, form=FormBook,extra=0, can_delete=True)
    ecrivain= get_object_or_404(Ecrivain, pk=id)
    ##
    form = FormEcr(request.POST or None,instance=ecrivain)
    formset = frmbook(request.POST or None,instance=ecrivain,prefix='ecrivains')

    if request.method == 'POST':
        
        #formset = frmfmvt(request.POST ,instance=nature,prefix='mouvement')
        if form.is_valid() and formset.is_valid() :
            
            try:
                with transaction.atomic():
                    ecr = form.save(commit=False)
                    ecr.save()
                  
                    for book in formset:
                        #print(mvt.cleaned_data)
                        data = book.save(commit=False)
                        data.ecrivain = ecr
                        data.save()
            except IntegrityError:
                print("Error Encountered")

    context = {'form':form,'formset':formset}
    return render(request,'app1/editbook.html',context)
def deletemvt(request):
    print("enter")
  
def addbook(request):
    context ={} 
    form = FormEcr(request.POST or None)
    BookFormSet = modelformset_factory(Book,form=FormBook, extra = 1) 
    formset = BookFormSet(request.POST or None,queryset= Book.objects.none(),prefix='ecrivains')
    if request.method == "POST":
        #return HttpResponse(formset)
        if form.is_valid() and formset.is_valid():
            
            try:
                with transaction.atomic():
                    ecr = form.save(commit=False)
                    ecr.save()
                    for book in formset:
                        data = book.save(commit=False)
                        data.ecrivain = ecr
                        data.save()
            except IntegrityError:
                print("Error Encountered")
    context['formset'] = formset
    context['form'] = form
    return render(request, 'app1/home.html', context)
 

def index(request):
    #print("jouami",request.user.id)
    myDate = datetime.now()
    personnes= Personne.objects.filter(user_id=request.user.id)
    return render(request,'app1/first.html',{"personnes":personnes,'wnom':'hhhhhh','myDate':myDate})

def add_pers(request):
    if request.method == "POST":
        form= FormPers(request.POST)
        if form.is_valid():
            #form.save()
            datenais = form.cleaned_data['date_nais'] 
            wdate1 = form.cleaned_data['date_of_birth'] 
            wdate2 = form.cleaned_data['date_of_death'] 
            wdat_conv1= datetime.strptime(str(wdate1), "%Y-%m-%d").date()
            wdat_conv2= datetime.strptime(str(wdate2), "%Y-%m-%d").date()
            #a = datetime.strptime(str(wdate1), date_format)
            #b = datetime.strptime(str(wdate2), date_format)
            delta = wdat_conv2 - wdat_conv1
            t = "2020-10-31"
            print(calendar.month_abbr[datenais.month], "-", calendar.month_name[datenais.month])
            #print(calendar.month_name[datenais.month])
            print(datenais.strftime('%B')) 
            print((wdate2-wdate1).days)
            #print(datetime.strptime(wdate1,"%Y-%m-%d"))
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
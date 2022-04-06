from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
from .forms import *

def home(request):
    doc_externo=loader.get_template('home.html')
    documento=doc_externo.render({})
    return HttpResponse(documento)
# Create your views here.

def logedHome(request):
    doc_externo=loader.get_template('logedHome.html')
    documento=doc_externo.render({})
    return HttpResponse(documento)

#def register(request):
#    return render()

#antes de hacer esto me conviene hacer el curso de mi mundo python
def register(request):
    if request.method=='POST':  #post is an html method thar uploads data to the sever's database, the get methos is used to request data from the server
       form=UserRegisterForm(request.POST)
       if form.is_valid():
            username=form.cleaned_data['username']
            #messages.succes(request,f'usuario {username} creado')
            #para colocar el mensage tengo que copiar el div de mensage en el html , y tengo que agregar el css de menssages a mi css
            return redirect('home')
    else:
        form=UserRegisterForm()
    context={'form':form}
    return render(request,'register.html',context)

def login(request):
    context={'form':form}
    return render(request,'register.html',context)

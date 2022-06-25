from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def teste(request):
    return HttpResponse('teste')

def inicio(request):
    return render(request,'apps/index.html')

def login(request):
    return render(request,'apps/login.html')    

def base(request):
    return render(request, 'templates/base.html')

def sobre(request):
    return render(request, 'apps/sobre.html')

def adminarea(request):
    return render(request, 'apps/adminarea.html')

def profissionais(request):
    return render(request, 'apps/profissionais.html')
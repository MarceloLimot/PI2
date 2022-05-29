from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def teste(request):
    return HttpResponse('teste')

def inicio(request):
    return render(request,'apps/index.html')

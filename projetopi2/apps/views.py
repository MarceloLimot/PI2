from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, request
from .models import LoginPrestador, Login
import datetime
from .forms import LoginPrestadorForm
from django.contrib import messages

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

def contato(request):
    return render(request, 'apps/contato.html')

#def adminarea(request):
#    return render(request, 'apps/adminarea.html')

def profissionais(request):
    return render(request, 'apps/profissionais.html')

@login_required
def cadPrestador(request):
    if request.method == 'POST':
        form = LoginPrestadorForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return render(request,'apps/index.html')
        else:
            print('erro no formulario')
    else:
        form = LoginPrestadorForm()
        return render(request, 'apps/cadPrestador.html', {'form':form})


#------------------/Função para Listar Prestadores/-----------------#

#def listaPrestador(request):
#    listLogin = LoginPrestador.objects.all().order_by('-criado_em')
#    paginator = Paginator(listLogin, 2)
#    page = request.GET.get('page')
#    Login = paginator.get_page(page)
#    return render(request, 'apps/listaPrestador.html', {'logins':Login})

def listaPrestador(request):
    nome = LoginPrestador.objects.all()
    return render(request, 'apps/listaPrestador.html', {'loginPrestador':nome})

def listaAssistencia(request):
    nome = LoginPrestador.objects.filter(profissional__icontains = 'assistencia tecnica')
    return render(request, 'apps/listaPrestador.html', {'loginPrestador':nome})

def listaProfessor(request):
    nome =LoginPrestador.objects.filter(profissional__icontains = 'professor')
    return render(request, 'apps/listaPrestador.html', {'loginPrestador':nome})

def listaMecanico(request):
    nome = LoginPrestador.objects.filter(profissional__icontains = 'mecanico')
    return render(request, 'apps/listaPrestador.html', {'loginPrestador':nome})

def listaConsultoria(request):
    nome = LoginPrestador.objects.filter(profissional__icontains = 'consultoria')
    return render(request, 'apps/listaPrestador.html', {'loginPrestador':nome})

def listaTecnologia(request):
    nome =LoginPrestador.objects.filter(profissional__icontains = 'Tecnologia')
    return render(request, 'apps/listaPrestador.html', {'loginPrestador':nome})

def listaEventos(request):
    nome =LoginPrestador.objects.filter(profissional__icontains = 'eventos')
    return render(request, 'apps/listaPrestador.html', {'loginPrestador':nome})

def listaBeleza(request):
    nome =LoginPrestador.objects.filter(profissional__icontains = 'beleza')
    return render(request, 'apps/listaPrestador.html', {'loginPrestador':nome})

def listaReparos(request):
    nome =LoginPrestador.objects.filter(profissional__icontains = 'reparos')
    return render(request, 'apps/listaPrestador.html', {'loginPrestador':nome})

def listaSaude(request):
    nome =LoginPrestador.objects.filter(profissional__icontains = 'Saude')
    return render(request, 'apps/listaPrestador.html', {'loginPrestador':nome})

def listaDomestico(request):
    nome =LoginPrestador.objects.filter(profissional__icontains = 'domestico')
    return render(request, 'apps/listaPrestador.html', {'loginPrestador':nome})

def listaMotociclista(request):
    nome =LoginPrestador.objects.filter(profissional__icontains = 'motociclista')
    return render(request, 'apps/listaPrestador.html', {'loginPrestador':nome})
#------------------/Fim da Função para Listar Prestadores/-----------------#


#------------------/funcao para cadastro de Prestador\------------------#
@login_required
def prestador(request, id):
    nome = get_object_or_404(LoginPrestador, pk=id) 
    form = LoginPrestadorForm(instance= nome)

    if request.method == 'POST':
        form = LoginPrestadorForm(request.POST, instance= nome)
        if(form.is_valid()):
            func.save()
            return redirect('/')  
        else:
            return render(request,'apps/prestador.html',{'form': form, 'task':nome})                  
    else:
        return render(request,'apps/prestador.html',{'form': form, 'task':nome})
#---------------/Fim da funcao de cadastro de Prestador\---------------#

#----------------/Função para editar prestador\------------------#
@login_required
def editPrestador(request, id): 
    func = get_object_or_404(LoginPrestador, pk=id)
    form = LoginPrestadorForm(instance=func)

    if request.method == 'POST':
        form = LoginPrestadorForm(request.POST, instance=func)

        if(form.is_valid()):
            func.save()
            return redirect('/profissionais')  
        else:
            return render(request,'apps/editPrestador.html',{'form': form, 'task':func})                  
    else:
        return render(request,'apps/editPrestador.html',{'form': form, 'task':func})

########################################################################
                            #Deletar Logins#
########################################################################
#------------------/funcao para delete de Funcionario\------------------#
@login_required
def deletePrestador(request, id):
    func = get_object_or_404(LoginPrestador, pk=id)
    func.delete()
    return redirect('/profissionais')
#---------------/Fim da funcao para delete de Funcionario\---------------#

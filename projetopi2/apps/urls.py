from django.urls import path, include
from django.conf.urls.static import static

from . import views

urlpatterns = [
    #path('admin', admin.site.urls),
    path('', views.inicio),
    path('inicio', views.inicio, name='login'),
    path('sobre', views.sobre),
    path('login',views.login),
    path('contato',views.contato),
    #path('adminarea', views.adminarea, name='adminarea'),
    path('profissionais', views.profissionais),
    path('cadPrestador', views.cadPrestador, name='cadPrestador'),

    path('editPrestador/<int:id>',views.editPrestador),  

    path('deletePrestador/<int:id>',views.deletePrestador, name='deletePrestador'),
#-------------------------Listagem de Profissionais-------------------------------#
    path('listaPrestador', views.listaPrestador, name='listaPrestador'),
    path('listaAssistencia', views.listaAssistencia, name='listaAssistencia'),
    path('listaProfessor', views.listaProfessor, name='listaProfessor'),
    path('listaMecanico', views.listaMecanico, name='listaMecanico'),
    path('listaConsultoria', views.listaConsultoria, name='listaConsultoria'),
    path('listaTecnologia', views.listaTecnologia, name='listaTecnologia'),
    path('listaEventos', views.listaEventos, name='listaEventos'),
    path('listaBeleza', views.listaBeleza, name='listaBeleza'),
    path('listaReparos', views.listaReparos, name='listaReparos'),
    path('listaSaude', views.listaSaude, name='listaSaude'),
    path('listaDomestico', views.listaDomestico, name='listaDomestico'),
    path('listaMotociclista', views.listaMotociclista, name='listaMotociclista'),
    #path('areadoador', views.areadoador, name='areadoador'),

    path('prestador/<int:id>', views.prestador, name='prestador'),

]
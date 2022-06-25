from django.urls import path, include

from . import views

urlpatterns = [
    #path('admin', admin.site.urls),
    path('', views.inicio),
    path('inicio', views.inicio, name='login'),
    path('sobre', views.sobre),
    path('login',views.login),
    path('adminarea', views.adminarea, name='adminarea'),
    path('profissionais', views.profissionais),
    #path('areadoador', views.areadoador, name='areadoador'),
]
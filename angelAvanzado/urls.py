"""
URL configuration for angelAvanzado project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tendoApp import views


urlpatterns = [
    path('', views.home, name='home'),
    path('task/', views.task, name='task'),
    path('task/addtask/', views.addtask, name='addtask'),
    path('task/<int:task_id>/update/', views.updateTask, name='update_task'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('singUp/', views.singUp, name='singUp'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('paises/', views.lista_paises, name='lista_paises'),
    path('ciudades/', views.lista_ciudades, name='lista_ciudades'),

    path('ciudades/por_pais/<int:pais_id>/', views.ciudades_por_pais, name='ciudades_por_pais'),
    path('ciudades/<int:ciudad_id>/eliminar/', views.eliminar_ciudad, name='eliminar_ciudad'),
]

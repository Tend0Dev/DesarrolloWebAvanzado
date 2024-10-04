from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from .models import Task
from .forms import TaskForm

from .models import Pais, Ciudad
from .forms import PaisForm, CiudadForm
from django.http import JsonResponse
from collections import defaultdict


def home(request):
    return render(request, 'home.html')


def task(request):
    tasks = Task.objects.all()
    return render(request, 'task.html', {
        'tasks': tasks
        })


def addtask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('task')
        else:
            form = TaskForm()
            return render(request, 'addtask.html', {'form': form})



    

def singUp(request):
    if request.method == 'GET':
        return render(request, 'singUp.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('task')
            except:
                return render(request, 'singUp.html',{
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe' 
                    })
        else: 
            return render(request, 'singUp.html',{
                'form': UserCreationForm,
                'error': 'contraseña no coincide'
                })
            


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], 
                            password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'Usuario y contraseña no coinciden'
        })
        else:
            login(request, user)
            return redirect('task')
    
def signout(request):
    logout(request)
    return redirect('home')


def updateTask(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task_list = Task.objects.all()  

    if request.method == 'GET':
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {
            'task': task,
            'form': form,
            'task_list': task_list
        })
    else:
        try:
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('task')
        except ValueError:
            return render(request, 'task_detail.html', {
                'task': task,
                'form': form,
                'task_list': task_list,
                'error': 'Error al actualizar la tarea'
            })
        

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)  
    return render(request, 'task_detail.html', {
        'task': task
    })

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})



def lista_paises(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_paises')
    else:
        form = PaisForm()
    
    paises = Pais.objects.all()
    return render(request, 'lista_paises.html', {'form': form, 'paises': paises})


def lista_ciudades(request):
    if request.method == 'POST':
        form = CiudadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ciudades')
    else:
        form = CiudadForm()
    
    # Agrupar ciudades por país
    ciudades_por_pais = defaultdict(list)
    for ciudad in Ciudad.objects.all().select_related('pais'):
        ciudades_por_pais[ciudad.pais].append(ciudad)
    
    return render(request, 'lista_ciudades.html', {
        'form': form, 
        'ciudades_por_pais': dict(ciudades_por_pais)
    })

def agregar_ciudad(request):
    if request.method == 'POST':
        form = CiudadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ciudades')
    else:
        form = CiudadForm()
    return render(request, 'agregar_ciudad.html', {'form': form})

def ciudades_por_pais(request, pais_id):
    pais = get_object_or_404(Pais, id=pais_id)
    ciudades = pais.ciudades.all()
    return JsonResponse(list(ciudades.values('id', 'nombre')), safe=False)

def eliminar_ciudad(request, ciudad_id):
    ciudad = get_object_or_404(Ciudad, id=ciudad_id)
    if request.method == 'POST':
        ciudad.delete()
        return redirect('lista_ciudades')
    return render(request, 'confirmar_eliminar_ciudad.html', {'ciudad': ciudad})

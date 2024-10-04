from django.forms import ModelForm
from django import forms
from .models import Task
from .models import Pais, Ciudad


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre']

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['nombre', 'pais']
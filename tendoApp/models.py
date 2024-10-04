from django.db import models
from django.contrib.auth.models import User

# Create your models here.



# Create your models here.
class Task(models.Model):
    title = models.CharField( max_length=100, verbose_name='titulo')
    description = models.TextField(blank=True, verbose_name='description')
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    datecompleted = models.DateTimeField(null=True, verbose_name='fecha completado')
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return self.title + ' by ' + self.user.username
    
class Pais(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='ciudades')

    def __str__(self):
        return f"{self.nombre}, {self.pais.nombre}"
from unittest.util import _MAX_LENGTH
from django.db import models
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.db import models
from operator import truediv
from statistics import mode


class Curso(models.Model):
    User= models.CharField(max_length=40)
    Clave= models.IntegerField()

class Estudiante(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()

#loggin

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="avatars", null=True, blank=True)

#blog

class BlogModel(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

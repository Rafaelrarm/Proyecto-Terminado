from django.contrib import admin
from django.urls import path
from mi_app.views import (saludo, saludar_a, 
listar_cursos, listar_estudiantes, formulario_curso, formulario_busqueda, blog_personal)


urlpatterns = [
    
    path('saludar/', saludo),
    path('saludar/persona/<nombre>', saludar_a),
    path('listar-cursos/', listar_cursos),
    path('listar-estudiantes/', listar_estudiantes),
    path('formulario/', formulario_curso),
    path('buscar/', formulario_busqueda),
    path('blog/', blog_personal),
    
    ]

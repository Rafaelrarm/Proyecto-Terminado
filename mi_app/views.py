from django.shortcuts import render
from django.http import HttpResponse
from mi_app.models import Curso, Estudiante
from mi_app.forms import CursoFormulario, CursoBusquedaFormulario

def saludo(request):
    return HttpResponse("hola mundo")

    def __str__(self):
        return self.nombre

def saludar_a(request, nombre):
    return HttpResponse(f"hola como estas {nombre.capitalize()}")

def listar_cursos(request):
    context= {}
    context["cursos"]= Curso.objects.all()
    return render(request, "mi_app/lista_cursos.html", context)

def listar_estudiantes(request):
    context= {}
    context["estudiantes"]= Estudiante.objects.all()
    return render(request, "mi_app/lista_estudiantes.html", context)

def formulario_curso(request):

    if request.method == 'POST':

        mi_formulario = CursoFormulario(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            curso = Curso (nombre=informacion['curso'], camada=informacion['camada'])

            curso.save()

            return render(request, "mi_app/blog.html")
        pass
    else:

        mi_formulario= CursoFormulario()

        return render(request, "mi_app/curso_formulario.html", {"mi_formulario":mi_formulario})


def formulario_busqueda(request):

    busqueda_formulario = CursoBusquedaFormulario()

    if request.GET:
        
        cursos = Curso.objects.filter(nombre=busqueda_formulario["criterio"]).all()

        return render(request, "mi_app/curso_busqueda.html", {"cursos": cursos})

    return render(request, "mi_app/curso_busqueda.html", {"busqueda_formulario": busqueda_formulario})

def blog_personal(request):
    return render (request, "mi_app/blog.html",{})



from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, TemplateView, View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from mi_app.models import Curso, Estudiante, BlogModel, Avatar
from mi_app.forms import CursoFormulario, CursoBusquedaFormulario
from multiprocessing import context
from datetime import date, datetime


def __str__(self):
        return self.nombre

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

            curso = Curso(User=informacion['User'], Clave=informacion['Clave'])

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

#loggin

class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'mi_app/blogger_crear_cuenta_form.html'
  success_url = reverse_lazy('blog_login')
  form_class = UserCreationForm
  success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"

class BloggerProfile(DetailView):

    model = Avatar
    template_name = "mi_app/blogger_detail.html"

class UserUpdate(LoginRequiredMixin, UpdateView):

    model = User
    template_name = "mi_app/user_form.html"
    fields = ["username", "email", "first_name", "last_name"]

    def get_success_url(self):
      return reverse_lazy("user-detail", kwargs={"pk": self.request.user.id})

#blog

class BlogList(ListView):

    model = BlogModel
    template_name = "mi_app/blog_list.html"


class BlogDetail(DetailView):

    model = BlogModel
    template_name = "mi_app/blog_detail.html"


class BlogCreate(LoginRequiredMixin, CreateView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")
    fields = ["titulo", "sub_titulo", "cuerpo"]

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class BlogUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")
    fields = ["titulo", "sub_titulo", "cuerpo"]

    def test_func(self):
        exist = BlogModel.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False
        


class BlogDelete(LoginRequiredMixin,UserPassesTestMixin, DeleteView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")

    def test_func(self):
        exist = BlogModel.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False


class BlogLogin(LoginView):
    template_name = 'mi_app/blog_login.html'
    next_page = reverse_lazy("blog_list")


class BlogLogout(LogoutView):
    template_name = 'mi_app/blog_logout.html'
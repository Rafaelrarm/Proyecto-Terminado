from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from mi_app.views import (listar_cursos, listar_estudiantes, 
formulario_curso, formulario_busqueda, blog_personal)
from mi_app import views


urlpatterns = [
    
    path('listar-cursos/', listar_cursos),
    path('listar-estudiantes/', listar_estudiantes),
    path('formulario/', formulario_curso),
    path('buscar/', formulario_busqueda),
    path('blog/', blog_personal),

    #loggin
    path("crear/", views.SignUpView.as_view(), name ="blogger_signup"),
    path("profile/<pk>/", views.BloggerProfile.as_view(), name ="user-detail"),
    path("editar/<pk>/", views.UserUpdate.as_view(), name ="User-update"),

    #blog
    path("", views.BlogList.as_view(), name="blog_list"),
    path("crearblog/", views.BlogCreate.as_view(), name="blog_create"),
    path("detalle/<pk>/", views.BlogDetail.as_view(), name ="blog_detail"),
    path("editarblog/<pk>/", views.BlogUpdate.as_view(), name ="blog_update"),
    path("borrar/<pk>/", views.BlogDelete.as_view(), name ="blog_delete"),
    path("entrar/", views.BlogLogin.as_view(), name="blog_login"),
    path("salir/", views.BlogLogout.as_view(), name="blog_logout"),

    
    ]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.shortcuts import render
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("hola mundo")

def saludar_a(request, nombre):
    return HttpResponse(f"hola como estas {nombre.capitalize()}")

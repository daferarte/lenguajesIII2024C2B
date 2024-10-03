from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hola estudiantes desde usuarios</h1>")

def add(request):
    return HttpResponse("<h1>Bienvenidos a agregar ussuarios</h1>")

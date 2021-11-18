from django.shortcuts import render

from .models import Usuario

# Create your views here.

def Usuarios(request):


    todos_usuarios = Usuario.objects.all()

    return render(request, "index.html", context ={"nome_pagina":  "Início da Dashboard",
                                                   "todos_usuarios": todos_usuarios, })
    
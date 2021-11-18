from django.shortcuts import render

# Create your views here.

def indexPorteiro(request):

    context = {

        "nome_pagina":  "Início da Dashboard",

    }
    
    return render(request, "index.html", context)
    
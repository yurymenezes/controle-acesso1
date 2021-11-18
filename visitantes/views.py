
from .models import Visitante
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from visitantes.forms import VisitanteForm, AutorizaVisitanteForm
from django.utils import timezone

# Create your views here.

def index(request):
    

    todos_visitantes = Visitante.objects.all()

    return render(request, "index.html", context ={"nome_pagina":  "Início da Dashboard",
                                                   "todos_visitantes": todos_visitantes, })

def Registrar_visitante(request):
    
    #definindo variavel form recebendo VisitanteForm
    form = VisitanteForm

    #verificando se o metodo do request é igual a POST 
    if request.method == "POST" :

        #colocando os dados no form
        form = VisitanteForm(request.POST)
        
        #validando as infirmações
        if form.is_valid():

           #associando os dados do formulario com a variavel visitante
            visitante = form.save(commit=False)

            #amarrando o usuario logado ao campo registrado_por do formulario
            visitante.registrado_por = request.user.porteiro

            #por fim salvando as informações do formulario
            visitante.save()
            #mensagem de confirmação de registro
            messages.success(
                request, 
                "Visitante Registrado com Sucesso"
            )
            return redirect ("visitantes")# esse redirect leva para urls e depois leva pra viwer....path("", index, name="visitantes",),

    context = {

        "nome_pagina": "Registrar Visitante",
        "form": form
     }
    
    return render(request, "registrar_visitante.html", context)
    
def informacoes_visitantes(request, id):

    visitante = get_object_or_404(
        Visitante,
        id=id
    )

    form = AutorizaVisitanteForm()

    if request.method == "POST":
        form = AutorizaVisitanteForm(

            request.POST,
            instance=visitante
        )

        if form.is_valid():
            visitante = form.save(commit=False)

            visitante.status = "EM_VISITA"
            visitante.horario_autorizacao = timezone.now()
            visitante.save()

            messages.SUCCESS(

                request,
                "Entrada de Visitante Autorizada com Sucesso"
            )
            return redirect("index")

    context = {

        "nome_pagina": "informações de visitantes",
        "visitante": visitante,
        "form": form

    }

    return render(request, "informacoes_visitante.html", context)



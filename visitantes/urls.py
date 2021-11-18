from .views import informacoes_visitantes, Registrar_visitante, index


from django.urls import path


urlpatterns = [

    path("", index, name="visitantes",),
    path("visitantes/<int:id>/", informacoes_visitantes, name="informacoes_visitantes",),
    path("registrar-visitante/", Registrar_visitante, name="registrar-visitante",),
]
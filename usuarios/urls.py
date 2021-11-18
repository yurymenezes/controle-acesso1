from usuarios.views import Usuario


from django.urls import path


urlpatterns = [

    path("", Usuario, name="indexusuario",)
]
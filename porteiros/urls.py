from porteiros.views import indexPorteiro


from django.urls import path


urlpatterns = [

    path("", indexPorteiro, name="indexporteiro",)
]
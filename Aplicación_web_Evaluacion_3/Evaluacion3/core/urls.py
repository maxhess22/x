from django.urls import path
from .views import home,form,añadir,visualizacion



urlpatterns = [
    path('', home,name="home"),
    path('formulario', form, name="forma"),
    path("añadir", añadir, name="añadir"),
    path("visualizar", visualizacion, name="visualizar1"),

]

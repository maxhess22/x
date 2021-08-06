from django.urls import path
from .views import home,form_libro,visualizacion, listresults




urlpatterns = [
    path('home', home,name="home"),
    path("Añadir", form_libro, name="añadir"),
    path("visualizar", visualizacion, name="visualizar1"),
    path("descarga", listresults, name="descarga"),
    
]

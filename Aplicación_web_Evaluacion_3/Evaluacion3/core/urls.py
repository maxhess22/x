from django.urls import path
from .views import (home,form_libro,visualizacion, excel, 
                        actualizacion, delete)




urlpatterns = [
    path('', home,name="home"),
    path("Añadir", form_libro, name="añadir"),
    path("visualizar", visualizacion, name="visualizar1"),
    path("descarga", excel, name="descarga"),
    path("actualizacion/<id>", actualizacion, name= "actualizacion"),
    path("borrar/<id>", delete, name= "borrar"),

    
]

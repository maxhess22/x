from django.urls import path
from .views import home,form,form_libro,visualizacion, testBasehtml




urlpatterns = [
    path('', home,name="home"),
    path('formulario', form, name="forma"),
    path("Añadir", form_libro, name="añadir"),
    path("visualizar", visualizacion, name="visualizar1"),
    path('hola', testBasehtml, name="testBasehtml" )

]

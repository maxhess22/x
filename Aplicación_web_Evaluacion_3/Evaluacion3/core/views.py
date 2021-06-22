from django.shortcuts import render
from .models import libro

def form(request):   
    return render(request,'core/Formulario.html')


def home(request):
  
    return render(request,'core/home.html')


def añadir(request):
    return render(request,'core/AgregarDatos.html')


def visualizacion(request):
    libros = libro.objects.all()
    datos ={ 'libros':libros}
    return render(request,'core/MostratDtatos.html',datos)




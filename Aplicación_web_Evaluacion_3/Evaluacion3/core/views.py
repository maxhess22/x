from django.shortcuts import render
from django.template import loader
from .models import Libro,Categoria_libro
from django.forms import ModelForm
from .forms import LibroForm

def form(request):   
    return render(request,'core/Formulario.html')


def home(request):
  
    
    return render(request,'core/home.html')


def form_libro(request):
    datos ={ 'form': LibroForm()}
    if request.method== 'POST':
        Formulario = LibroForm(request.POST)
        if Formulario.is_valid:
            Formulario.save()
            datos['mensaje'] = "Guardados correctamente"

    return render(request,'core/form_libro.html', datos)


def visualizacion(request):
    libros = Libro.objects.all()
    datos ={ 'libros':libros}
    return render(request,'core/MostratDtatos.html',datos)

def testBasehtml(request):
    return render(request, 'core\hola.html')




from django.shortcuts import (render, get_object_or_404, 
                                HttpResponseRedirect)
from django.template import loader
from .models import Libro,Categoria_libro
from django.forms import ModelForm
from .forms import LibroForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from excel_response import ExcelResponse
from openpyxl import Workbook
from openpyxl.styles import Alignment,Border,Font,PatternFill,Side
from django_excel_response import ExcelResponse










@login_required
def home(request):
  
    
    return render(request,'core/home.html')

@login_required
def form_libro(request):
    datos ={ 'form': LibroForm()}
    if request.method== 'POST':
        Formulario = LibroForm(request.POST)
        mensaje = "correcto"
        if Formulario.is_valid:
            Formulario.save()
            messages.success(request, "logrado")
            datos['mensaje'] = "Guardados correctamente",True

    return render(request,'core/form_libro.html', datos)

@login_required
def visualizacion(request):
    libros = Libro.objects.all()
    datos ={ 'libros':libros}
    return render(request,'core/MostratDtatos.html',datos)

@login_required
def excel(request):
    data = []
    data.append([
        'nombre libro',
        'autor libro',
        'descripcion',
        'categoria libro',
    ])
    results = Libro.objects.all()
    for result in results:
  
        data.append([
            result.nombre_libro,
            result.autor_libro,
            result.descripcion_libro,
            result.categoria_libro.nombre_categoria,
        ])
    return ExcelResponse(data,'reportes de libros',font='name SimSum')
    
    
@login_required
def delete(request, id):

    libro = Libro.objects.get(id = id)
    libro.delete()

    return HttpResponseRedirect("/visualizar")








@login_required
def actualizacion(request, id):
    libro = Libro.objects.get(id = id)

    contexto = {
        'form': LibroForm(instance=libro)
    }

    if request.method== 'POST':
        
        formulario = LibroForm(data=request.POST,instance=libro)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect("/visualizar")
    
    return render(request, 'core/actualizacion.html', contexto)
 










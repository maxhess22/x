from django.shortcuts import render
from django.template import loader
from .models import Libro,Categoria_libro
from django.forms import ModelForm
from .forms import LibroForm
import django_excel as excel
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required





@login_required
def home(request):
  
    
    return render(request,'core/home.html')

@login_required
def form_libro(request):
    datos ={ 'form': LibroForm()}
    if request.method== 'POST':
        Formulario = LibroForm(request.POST)
        if Formulario.is_valid:
            Formulario.save()
            datos['mensaje'] = "Guardados correctamente"

    return render(request,'core/form_libro.html', datos)

@login_required
def visualizacion(request):
    libros = Libro.objects.all()
    datos ={ 'libros':libros}
    return render(request,'core/MostratDtatos.html',datos)

@login_required
def listresults(request):
    export = []
    # Se agregan los encabezados de las columnas
    export.append([
        'nombre libro',
        'autor libro',
        'descripcion',
        'categoria libro',
        ])

    # Se obtienen los datos de la tabla o model y se agregan al array
    results = Libro.objects.all()
    for result in results:
        # ejemplo para dar formato a fechas, estados (si/no, ok/fail) o
        # acceder a campos con relaciones y no solo al id
        export.append([
            result.nombre_libro,
            result.autor_libro,
            result.descripcion_libro,
            result.categoria_libro.nombre_categoria,
            ])

    # se transforma el array a una hoja de calculo en memoria
    sheet = excel.pe.Sheet(export)

    # se devuelve como "Response" el archivo para que se pueda "guardar"
    # en el navegador, es decir como hacer un "Download"
    return excel.make_response(sheet, "xlsx", file_name="TEST.csv")








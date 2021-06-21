from django.shortcuts import render

def form(request):
    return render(request,'core/Formulario.html')


def home(request):
    return render(request,'core/home.html')


def añadir(request):
    return render(request,'core/AgregarDatos.html')


def visualizacion(request):
    return render(request,'core/MostratDtatos.html')




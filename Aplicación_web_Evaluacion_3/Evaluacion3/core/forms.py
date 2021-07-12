from django import forms
from django.forms import ModelForm
from .models import libro


class LibroForm(forms.ModelForm):

    class Meta:
        model = libro
        fields =['id_libro', 'nombre_libro','autor_libro'
        ,'descripcion_libro','categoria_libro']
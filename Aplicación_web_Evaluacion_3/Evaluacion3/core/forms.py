from django import forms
from django.forms import ModelForm
from .models import Libro, Pais,Banco ,Categoria_libro
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin


class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields =[ 'nombre_libro','autor_libro'
        ,'descripcion_libro','categoria_libro']
        widgets = {
            'nombre_libro': forms.TextInput(attrs={'cols': 80, 'rows': 20, 
            'placeholder': 'nombre del libro' }),
            
            'autor_libro': forms.TextInput(attrs={'cols': 80, 'rows': 20, 
            'placeholder': 'autor del libro'}),

            'descripcion_libro': forms.TextInput(attrs={'cols': 80, 'rows': 20, 
            'placeholder': 'descripcion'}),

            'categoria_libro': AutocompleteSelect(
                Libro._meta.get_field('categoria_libro').remote_field,
            admin.site,)
    }


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['id_pais','nombre_pais']


class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = ['id_banco','nombre_banco']
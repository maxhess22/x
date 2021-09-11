from django import forms
from django.forms import ModelForm
from .models import Libro, Pais,Banco ,Categoria_libro
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin
from django_select2 import forms as s2forms





class CategoriaWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "nombre_categoria",
    ]



class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields =[ 'nombre_libro','autor_libro'
        ,'descripcion_libro','categoria_libro']
        widgets = {
            'nombre_libro': forms.TextInput(attrs={
            'placeholder': 'nombre del libro', 'class': 'form-control' }),
            
            'autor_libro': forms.TextInput(attrs={
            'placeholder': 'autor del libro', 'class': 'form-control'}),

            'descripcion_libro': forms.TextInput(attrs={
            'placeholder': 'descripcion', 'class': 'form-control'}),

            'categoria_libro': forms.Select(
                attrs={'class': 'form-control select2 '}),
    }


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['id_pais','nombre_pais']


class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = ['id_banco','nombre_banco']
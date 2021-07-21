from django import forms
from django.forms import ModelForm
from .models import libro


class LibroForm(forms.ModelForm):

    class Meta:
        model = libro
        fields =['id_libro', 'nombre_libro','autor_libro'
        ,'descripcion_libro','categoria_libro']
        widgets = {

            'id_libro' : forms.NumberInput(attrs={'cols': 80, 'rows': 20,
            'placeholder': 'id libro'}), 

            'nombre_libro': forms.TextInput(attrs={'cols': 80, 'rows': 20, 
            'placeholder': 'nombre del libro' }),
            
            'autor_libro': forms.TextInput(attrs={'cols': 80, 'rows': 20, 
            'placeholder': 'autor del libro'}),

            'descripcion_libro': forms.TextInput(attrs={'cols': 80, 'rows': 20, 
            'placeholder': 'descripcion'}),
    
    }
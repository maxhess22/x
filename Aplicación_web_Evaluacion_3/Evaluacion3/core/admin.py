from django.contrib import admin
from .models import Libro,Categoria_libro,Banco,Pais




class Categoria_libroAdmin(admin.ModelAdmin):
    search_fields = ('nombre_categoria'),
    ordering = ['nombre_categoria']

class LibroAdmin(admin.ModelAdmin):
    
    ordering = ['nombre_libro']
    autocomplete_fields = ['categoria_libro']
    







admin.site.register(Libro, LibroAdmin)
admin.site.register(Categoria_libro, Categoria_libroAdmin )
admin.site.register(Banco)
admin.site.register(Pais)




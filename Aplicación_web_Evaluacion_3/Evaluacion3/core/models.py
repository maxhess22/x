from django.db import models    



class categoria_libro(models.Model):
    id_categoria= models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50)

  


class libro(models.Model):
    id_libro = models.IntegerField(primary_key=True)
    nombre_libro = models.CharField(max_length=50)
    autor_libro = models.CharField(max_length=50)
    descripcion_libro = models.CharField(max_length=50)
    categoria_libro = models.ForeignKey( categoria_libro, on_delete=models.CASCADE)
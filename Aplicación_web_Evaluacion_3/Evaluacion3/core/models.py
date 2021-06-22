from django.db import models    



class categoria_libro(models.Model):
    nombre_categoria = models.CharField(max_length=50)

  


class libro(models.Model):
    nombre_libro = models.CharField(max_length=50)
    autor_libro = models.CharField(max_length=50)
    descripcion_libro = models.CharField(max_length=50)
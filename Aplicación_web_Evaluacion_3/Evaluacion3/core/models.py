from django.db import models    



class Categoria_libro(models.Model):
    id_categoria= models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre_categoria



    

class Pais(models.Model):
    id_pais = models.IntegerField(primary_key=True)
    nombre_pais = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre_pais



class Banco(models.Model):
    id_banco = models.IntegerField(primary_key=True )
    nombre_banco = models.CharField(max_length=50)
    horario1 = models.BooleanField(default=False, verbose_name="De 00:00 a 02:00")
    horario2 = models.BooleanField(default=False, verbose_name="De 02:00 a 04:00")
    Pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_banco  





class Libro(models.Model):
    nombre_libro = models.CharField(max_length=50, verbose_name = "Nombre del libro" )
    autor_libro = models.CharField(max_length=50, verbose_name = "Autor del libro")
    descripcion_libro = models.CharField(max_length=50, verbose_name = "Descripcion del libro")
    categoria_libro = models.ForeignKey( Categoria_libro, on_delete=models.CASCADE)
    








class Ciudad(models.Model):
    id_ciudad = models.IntegerField(primary_key=True)
    nombre_ciudad =  models.CharField(max_length=50)
    def __str__(self):
        return self.nombre_ciudad


 







from django.db import models

class Categoria(models.Model):
	nombreCat=models.CharField(max_length=50)

class Producto(models.Model):
	nomProducto = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=100)
	costo = models.CharField(max_length=10)
	disponibilidad= models.BooleanField(default=False)
	categoria = models.ForeignKey(Categoria,null=True,blank=True, on_delete = models.CASCADE)
		


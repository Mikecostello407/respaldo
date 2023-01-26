from django.db import models

# Create your models here.

#Modelo para la categoria
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCatgoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoría')
    def __str__(self):
        return self.nombreCatgoria


#Modelo para el Vehiculo
class Vehiculo(models.Model):
    patente = models.CharField(max_length=8, primary_key=True, verbose_name='Patente')
    marca = models.CharField(max_length=20, verbose_name='Marca del Vehículo')
    modelo = models.CharField(max_length=20, null=True, verbose_name='Modelo')
    anio = models.CharField(max_length=4, verbose_name='año')
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    def __str__(self):
        return self.patente




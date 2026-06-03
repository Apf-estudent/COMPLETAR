from django.db import models
from deposito.models import Deposito

class Estado(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion

class Nivel_Riesgo(models.Model):
    id_nivel_de_riesgo = models.AutoField(primary_key=True)
    nombre_riesgo = models.CharField(max_length=100, default="Bajo") 

    def __str__(self):
        return self.nombre_riesgo

# CAMBIADO AQUÍ: Clase en singular para que combine con tus URLs
class Medicamento(models.Model): 
    id_medicamento = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=250)
    fechadevencimiento = models.DateField()
    lote = models.CharField(max_length=100) 
    fechadeingreso = models.DateField()
    fechadedispensa = models.DateField(blank=True, null=True) 
    id_deposito = models.ForeignKey(Deposito, on_delete=models.CASCADE)
    
    # CAMBIADO AQUÍ: Carpeta de subida en singular
    qr = models.ImageField(upload_to="medicamento/qr/", blank=True, null=True)
    
    codigo_barras = models.BigIntegerField() 
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    refrigeracion = models.CharField(max_length=200) 
    id_nivel_de_riesgo = models.ForeignKey(Nivel_Riesgo, on_delete=models.CASCADE)
    cant_stock = models.IntegerField() 

    def __str__(self):
        return self.descripcion
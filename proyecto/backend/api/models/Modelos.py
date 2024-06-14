from django.db import models

class Cliente(models.Model):
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    
    def __str__(self):
        return self.cedula
    
class Servicio(models.Model):
    
    nombre_servicio = models.CharField(max_length=100)
    cedula_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_servicio
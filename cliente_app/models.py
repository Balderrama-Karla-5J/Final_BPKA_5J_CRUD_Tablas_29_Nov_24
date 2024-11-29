from django.db import models

# Create your models here.
class Clientes(models.Model):
    id_cliente = models.PositiveBigIntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    direccion = models.CharField(null=False, max_length=50)
    telefono = models.CharField(max_length=13, null=False)
    correo = models.EmailField()
    edad = models.PositiveBigIntegerField(null=False)
    sexo = models.CharField(null=False, max_length=10)

    def __str__(self):
        return self.nombre
from django.db import models

# Create your models here.
class Empleados(models.Model):
    id_empleado = models.PositiveBigIntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    direccion = models.CharField(null=False, max_length=50)
    telefono = models.PositiveBigIntegerField(null=False)
    salario = models.FloatField()
    edad = models.PositiveBigIntegerField(null=False)
    sexo = models.CharField(null=False, max_length=10)

    def __str__(self):
        return self.nombre
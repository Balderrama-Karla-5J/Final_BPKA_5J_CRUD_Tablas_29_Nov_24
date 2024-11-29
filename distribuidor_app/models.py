from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Distribuidor(models.Model):
    id_distribuidor = models.PositiveBigIntegerField(null=False, primary_key=True)
    costo = models.TextField( max_length=10,null=False)
    numentregas = models.PositiveIntegerField()
    telefono = models.TextField(max_length=12,null=False)
    correo = models.EmailField(null=False)
    nombre = models.TextField(max_length=60,null=False)
    ciudad = models.TextField(max_length=50,null=False)

    def __str__(self):
        return self.nombre
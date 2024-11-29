from django.db import models

# Create your models here.
class Sucursal(models.Model):
    id_sucursal = models.PositiveBigIntegerField(null=False, primary_key=True)
    txtdireccion = models.CharField(max_length=50, null=False)
    numtelefono = models.CharField(null=False, max_length=50)
    txtcorreo = models.CharField(null=False, max_length=50)
    numstock = models.PositiveIntegerField()
    numempleados = models.PositiveIntegerField(null=False)
    txthorario = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.id_sucursal
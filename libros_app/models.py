from django.db import models

# Create your models here.
class Libros(models.Model):
    id_libro = models.PositiveBigIntegerField(null=False, primary_key=True)
    titulo = models.CharField(max_length=50, null=False)
    autor = models.CharField(null=False, max_length=50)
    ilustrador = models.CharField(null=False, max_length=50)
    año = models.DateField()
    precio = models.FloatField(null=False)
    stock = models.PositiveIntegerField(null=False )

    def __str__(self):
        return self.titulo
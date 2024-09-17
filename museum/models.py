from django.db import models


# Create your models here.
class Museum(models.Model):

    name = models.CharField(max_length=50,  default=None)
    latitud = models.DecimalField(decimal_places=5, max_digits = 20, default=None)
    longitud = models.DecimalField(decimal_places=5, max_digits=20,  default=None)
    category = models.CharField(max_length=50, default='Unknown Category')
    city = models.CharField(max_length=50, default='Unknown City')
    country = models.CharField(max_length=50, default='Unknown Country')
    description = models.CharField(max_length=50, default='Unknown Description')



    def __str__(self) -> str:
        return '{}'.format(self.name)

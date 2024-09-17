from django.db import models
from museum.models import Museum
from artist.models import Artist

# Create your models here.
class Artwork(models.Model):

    name = models.CharField(max_length=50, default=None)
    date = models.DateField(default=None)
    technique = models.CharField(max_length=50, default=None)
    dimensions = models.CharField(max_length=50, default=None)
    preview = models.CharField(max_length=50, default=None)
    advancedInfo = models.CharField(max_length=50, default=None)


    #Relacion con museo
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE, default=None)
    

    #Relacion artist
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, default=None)
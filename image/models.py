from django.db import models
from museum.models import Museum
from artwork.models import Artwork
from artist.models import Artist

# Create your models here.
class Image(models.Model):

    url = models.URLField(max_length=200)
    descripcion = models.CharField(max_length=500)


    #Relacion con museum
    museum = models.ForeignKey(
        Museum,
        on_delete=models.SET_NULL,
        null = True,
        blank=True
    )

    #Relacion con Artwork
    artwork = models.OneToOneField(
        Artwork,
        on_delete=models.SET_NULL,
        null = True,
        blank=True
    )

    #Relacion con Artist
    artist = models.ForeignKey(
        Artist,
        on_delete=models.SET_NULL,
        null = True,
        blank=True
    )
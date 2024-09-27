from django.db import models
from artwork.models import Artwork

# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=50, default=None)
    userName = models.CharField(max_length=50, unique=True, default=None)
    email = models.EmailField(max_length=254, unique=True, default=None)
    password = models.CharField(max_length=50, default=None)

    #Relacion con artwork
    likedArtowks = models.ManyToManyField(Artwork, related_name='usersLiked', blank=True)
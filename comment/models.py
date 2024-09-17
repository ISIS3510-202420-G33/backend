from django.db import models
from artwork.models import Artwork
from user.models import User

# Create your models here.
class Comment (models.Model):

    content = models.CharField(max_length=200)
    date = models.DateField()

    #Relacion con Artwork
    artwork = models.ForeignKey(
        Artwork,
        on_delete=models.CASCADE,
        default=None
    )

    #Relacion con Usuario
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None
    )
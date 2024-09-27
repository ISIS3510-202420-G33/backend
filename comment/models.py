from django.db import models
from artwork.models import Artwork
from user.models import User

# Create your models here.
class Comment (models.Model):

    content = models.CharField(max_length=400)
    date = models.DateField()

    #Relacion con Artwork
    artwork = models.ForeignKey(
        Artwork,
        on_delete=models.CASCADE,
        default=None,
        related_name='comments'
    )

    #Relacion con Usuario
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None
    )
from django.db import models

# Create your models here.
class Artist(models.Model):

    name = models.CharField(max_length=50,  default=None)
    biography = models.CharField(max_length=50,  default=None)

    
    
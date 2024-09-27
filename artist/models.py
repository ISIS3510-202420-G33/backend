from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    image = models.CharField(max_length=500, default=None)

    def __str__(self):
        return self.name
    
    
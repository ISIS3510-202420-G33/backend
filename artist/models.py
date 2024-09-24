from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    image = models.ImageField(upload_to='artists/', null=False, blank=False)

    def __str__(self):
        return self.name
    
    
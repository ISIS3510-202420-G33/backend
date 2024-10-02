from django.db import models
from django.utils import timezone
from user.models import User  
from artwork.models import Artwork  

class LikeHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)  
    date_liked = models.DateField(default=timezone.now) 

    def __str__(self):
        return f"{self.user} liked {self.artwork} on {self.date_liked}"

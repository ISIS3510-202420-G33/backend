from user.models import User
from artwork.models import Artwork
from django.db.models import Q

def recommend_artworks(userId):
    try:
        user = User.objects.get(pk=userId)
        
        liked_artworks = user.likedArtowks.all()
        print(liked_artworks)

        if not liked_artworks.exists():
            return []

        artist_ids = liked_artworks.values_list('artist_id', flat=True)
        museum_ids = liked_artworks.values_list('museum_id', flat=True)

        recommended_artworks = Artwork.objects.filter(
            Q(artist_id__in=artist_ids) | Q(museum_id__in=museum_ids)
        ).exclude(id__in=liked_artworks.values_list('id', flat=True))

        return recommended_artworks
    
    except User.DoesNotExist:
        return "UserError"
    
    except Exception as e:
        return f"Error: {str(e)}"
       
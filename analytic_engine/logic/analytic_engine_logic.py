from user.models import User
from artwork.models import Artwork
from django.db.models import Q
import math
from museum.models import Museum  # Suponiendo que tienes un modelo de museo


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



def get_nearest_museums(user_latitude, user_longitude):
    try:
        # Obtén todos los museos
        all_museums = Museum.objects.all()

        # Crea una lista de tuplas (museo, distancia)
        museum_distances = []

        for museum in all_museums:
            distance = haversine_distance(user_latitude, user_longitude, museum.latitude, museum.longitude)
            museum_distances.append((museum, distance))

        # Ordena la lista por distancia (ascendente)
        museum_distances.sort(key=lambda x: x[1])

        # Devuelve los tres museos más cercanos
        nearest_museums = [museum for museum, distance in museum_distances[:3]]
        return nearest_museums

    except Exception as e:
        return f"Error: {str(e)}"
    

def haversine_distance(lat1, lon1, lat2, lon2):
    # Radio de la Tierra en kilómetros
    R = 6371.0
    
    # Convertir grados a radianes
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a = math.sin(d_lat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(d_lon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Distancia en kilómetros
    distance = R * c
    return distance

       
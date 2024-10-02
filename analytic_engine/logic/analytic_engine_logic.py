from user.models import User
from artwork.models import Artwork
from django.db.models import Q
import math
from museum.models import Museum
from likehistory.models import LikeHistory
from artwork.models import Artwork
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count

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
            user_latitude = float(user_latitude)
            user_longitude = float(user_latitude)
            latitude = float(museum.latitude)
            longitude = float(museum.longitude)
            distance = haversine_distance(user_latitude, user_longitude, latitude, longitude)
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

def get_most_liked_lastmonth():
    """
    Obtiene la obra con más likes en los últimos 30 días.
    """
    try:
        # Obtener la fecha de hace 30 días
        last_30_days = timezone.now().date() - timedelta(days=30)

        # Filtrar los likes de los últimos 30 días, agrupar por obra y contar
        most_liked = LikeHistory.objects.filter(date_liked__gte=last_30_days) \
                                        .values('artwork') \
                                        .annotate(like_count=Count('artwork')) \
                                        .order_by('-like_count') \
                                        .first()

        if most_liked:
            # Obtener la obra de arte más likeada
            artwork_id = most_liked['artwork']
            artwork = Artwork.objects.get(id=artwork_id)
            return artwork

        return None  # Si no hay obras con likes en los últimos 30 días

    except Exception as e:
        raise ValueError(f"Error fetching most liked artwork: {str(e)}")
       
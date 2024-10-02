from ..models import LikeHistory, User, Artwork
from django.utils import timezone

def add_like(user_id, artwork_id, date_liked=None):
    """
    Lógica para registrar un nuevo like en LikeHistory.
    user_id: ID del usuario que da like.
    artwork_id: ID de la obra de arte a la que se le da like.
    date_liked: Fecha en la que se da el like (opcional). Si no se proporciona, se usará la fecha y hora actuales.
    """
    if date_liked is None:
        date_liked = timezone.now()

    try:
        # Obtener el usuario y la obra de arte por su ID
        user = User.objects.get(pk=user_id)
        artwork = Artwork.objects.get(pk=artwork_id)

        # Crear un nuevo registro en LikeHistory
        like_history = LikeHistory.objects.create(
            user=user,
            artwork=artwork,
            date_liked=date_liked
        )

        return like_history

    except User.DoesNotExist:
        raise ValueError("User not found")
    except Artwork.DoesNotExist:
        raise ValueError("Artwork not found")

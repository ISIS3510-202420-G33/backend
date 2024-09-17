from ..models import Artist

def get_artist(var_pk):
    artist = Artist.objects.get(pk=var_pk)
    return artist
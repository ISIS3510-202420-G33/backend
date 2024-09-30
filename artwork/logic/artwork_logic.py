from ..models import Artwork, Artist

def get_artwork(var_pk):
    artwork = Artwork.objects.get(pk=var_pk)
    return artwork

def get_all_artworks():
    artworks= Artwork.objects.all()
    return artworks

def get_artworks_by_artist(artist_id):
    artworks = Artwork.objects.filter(artist_id=artist_id)
    return artworks

def get_comments(var_pk):
    artwork = Artwork.objects.get(pk=var_pk)
    comments = artwork.comments.all()
    return comments
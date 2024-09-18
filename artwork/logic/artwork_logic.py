from ..models import Artwork

def get_artwork(var_pk):
    artwork = Artwork.objects.get(pk=var_pk)
    return artwork

def get_comments(var_pk):
    artwork = Artwork.objects.get(pk=var_pk)
    comments = artwork.comments.all()
    return comments
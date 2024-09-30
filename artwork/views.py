from .logic import artwork_logic as al
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def artwork_view(request, pk):
    if request.method == 'GET':
        artwork = al.get_artwork(pk)
        artwork_dto = serializers.serialize('json', [artwork])
        return HttpResponse(artwork_dto, 'application/json')

def artworks_list_view(request):
    if request.method == 'GET':
        artworks = al.get_all_artworks()
        artworks_dto = serializers.serialize('json', artworks)
        return HttpResponse(artworks_dto, 'aplication/json')
    
def artwork_comments_view(request, pk):
     if request.method == 'GET':
        comments = al.get_comments(pk)
        comments_dto = serializers.serialize('json', comments)
        return HttpResponse(comments_dto, 'application/json')
    
def artworks_by_artist_view(request, pk):
    if request.method == 'GET':
        artworks = al.get_artworks_by_artist(pk)
        artworks_dto = serializers.serialize('json', artworks)
        return HttpResponse(artworks_dto, 'application/json')
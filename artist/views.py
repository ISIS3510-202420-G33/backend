from .logic import artist_logic as al
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def artist_view(request, pk):
    if request.method == 'GET':
        artist = al.get_artist(pk)
        artist_dto = serializers.serialize('json', [artist])
        return HttpResponse(artist_dto, 'application/json')
    
def artist_list_view(request):
    if request.method == 'GET':
        artists = al.get_all_artist()
        artists_dto = serializers.serialize('json', artists)
        return HttpResponse(artists_dto, 'aplication/json')
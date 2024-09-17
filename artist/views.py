from .logic import artist_logic as al
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def artist_view(request, pk):
    if request.method == 'GET':
        artist = al.get_artist(pk)
        artist_dto = serializers.serialize('json', [artist])
        return HttpResponse(artist_dto, 'application/json')
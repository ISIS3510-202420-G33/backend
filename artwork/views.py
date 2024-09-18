from .logic import artwork_logic as al
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def artwork_view(request, pk):
    if request.method == 'GET':
        artwork = al.get_artwork(pk)
        artwork_dto = serializers.serialize('json', [artwork])
        return HttpResponse(artwork_dto, 'application/json')
    
def artwork_comments_view(request, pk):
     if request.method == 'GET':
        comments = al.get_comments(pk)
        comments_dto = serializers.serialize('json', comments)
        return HttpResponse(comments_dto, 'application/json')
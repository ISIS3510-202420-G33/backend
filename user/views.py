import json
from django.http import HttpResponse
from django.core import serializers

from artwork.models import Artwork
from user.models import User
from .logic import user_logic as ul
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def user_view(request):

    if request.method == 'POST':
        user_dto = ul.create_user(json.loads(request.body))

        if user_dto == "Problema":
            return HttpResponse("Usuario o email ya existe", status=401, content_type='text/plain')


        user = serializers.serialize('json', [user_dto])
        return HttpResponse(user, 'application/json')
    
    
@csrf_exempt
def authenticate_view(request):
    if request.method == 'POST':
        user_dto = ul.authenticate_user(json.loads(request.body))

        if user_dto == "PassError":
            return HttpResponse("Invalid password", status=401, content_type='text/plain')
        
        elif user_dto == "UserError":
            return HttpResponse("Invalid User", status=401, content_type='text/plain')

        user = serializers.serialize('json', [user_dto])
        return HttpResponse(user, 'application/json')
    
@csrf_exempt
def like_view(request):
    if request.method == 'POST':
        user_dto = ul.like_artwork(json.loads(request.body))
        user = serializers.serialize('json', [user_dto])
        return HttpResponse(user, 'application/json')
   
@csrf_exempt
def unlike_view(request, user_id, artwork_id):
    if request.method == 'DELETE':
        try:
            user = User.objects.get(pk=user_id)
            artwork = Artwork.objects.get(pk=artwork_id)
            user.likedArtowks.remove(artwork)
            return HttpResponse(status=204)  # No content, éxito
        except User.DoesNotExist:
            return HttpResponse("User not found.", status=404)
        except Artwork.DoesNotExist:
            return HttpResponse("Artwork not found.", status=404)
    return HttpResponse("Invalid request method.", status=400)

def liked_view(request, pk):
    if request.method == 'GET':
        artworks_dto = ul.liked_arworks(pk)
        artworks = serializers.serialize('json', artworks_dto)
        return HttpResponse(artworks, 'application/json')

def users_view(request):
    if request.method == 'GET':
        users_dto = ul.get_users()
        users = serializers.serialize('json', users_dto)
        return HttpResponse(users, 'application/json')
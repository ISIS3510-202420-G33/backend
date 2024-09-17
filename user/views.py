import json
from django.http import HttpResponse
from django.core import serializers
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
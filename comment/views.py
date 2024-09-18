import json
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .logic import comment_logic as cl

# Create your views here.
@csrf_exempt
def comment_view(request):
    if request.method == 'POST':
        comment_dto = cl.comment_create(json.loads(request.body))
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        print(comment_dto.user)
        comment = serializers.serialize('json', [comment_dto])
        return HttpResponse(comment, 'application/json')
    
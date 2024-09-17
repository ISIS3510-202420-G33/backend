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
        user = serializers.serialize('json', [user_dto])
        return HttpResponse(user, 'application/json')

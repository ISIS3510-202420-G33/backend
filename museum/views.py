from django.http import HttpResponse
from django.core import serializers
from .logic import museum_logic as ml

# Create your views here.
def museums_view(request):
    if request.method== 'GET':
        museums = ml.get_museums()
        museums_dto = serializers.serialize('json', museums)
        return HttpResponse(museums_dto, 'application/json')
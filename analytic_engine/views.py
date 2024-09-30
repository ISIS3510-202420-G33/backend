from django.http import HttpResponse
from django.core import serializers

from .logic import analytic_engine_logic as ae
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def recommend_view(request, user_id):
    if request.method == 'GET':
        recommended_artworks_dto = ae.recommend_artworks(user_id)

        if recommended_artworks_dto == "UserError":
            return HttpResponse("User not found.", status=404)

        recommended_artworks = serializers.serialize('json', recommended_artworks_dto)
        return HttpResponse(recommended_artworks, 'application/json')

    return HttpResponse("Invalid request method.", status=400)

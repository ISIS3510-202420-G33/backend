from django.http import HttpResponse, JsonResponse
from django.core import serializers

from .logic import analytic_engine_logic as ae
from django.views.decorators.csrf import csrf_exempt
import json

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

@csrf_exempt
def nearest_museums_view(request):
    if request.method == 'POST':
        try:
            # Obtén la latitud y longitud del usuario desde el cuerpo de la solicitud
            data = json.loads(request.body)
            user_latitude = data.get('latitude')
            user_longitude = data.get('longitude')

            if user_latitude is None or user_longitude is None:
                return JsonResponse({'error': 'Missing latitude or longitude.'}, status=400)

            # Llama a la función para obtener los museos más cercanos
            nearest_museums = ae.get_nearest_museums(user_latitude, user_longitude)

            # Serializa los museos más cercanos a JSON
            museums_json = serializers.serialize('json', nearest_museums)
            return HttpResponse(museums_json, 'application/json')

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON input.'}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)

def most_liked_artwork_view(request):
    if request.method == 'GET':
        try:
            # Llamar a la lógica para obtener la obra con más likes
            result = ae.get_most_liked_lastmonth()

            if result:
                artwork_dto = serializers.serialize('json', [result])
                return HttpResponse(artwork_dto, 'application/json')

            return JsonResponse({'message': 'No artworks liked in the last 30 days'}, status=404)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def spotlight_artworks_view(request):
    if request.method == 'GET':
        try:
            # Llamar a la lógica para obtener las obras promocionadas
            spotlight_artworks = ae.get_spotlight_artworks()

            if spotlight_artworks:
                artworks_dto = serializers.serialize('json', spotlight_artworks)
                return HttpResponse(artworks_dto, 'application/json')
            
            return JsonResponse({'message': 'No spotlight artworks found'}, status=404)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
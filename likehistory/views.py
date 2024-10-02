from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .logic import likehistory_logic as lk  # Importas la lógica con alias 'lk'


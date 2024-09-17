from ..models import Museum

def get_museums():
    museums = Museum.objects.all()
    return museums

def get_museum(museum_pk):
    museum = Museum.objects.get(pk=museum_pk)
    return museum
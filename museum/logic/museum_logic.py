from ..models import Museum

def get_museums():
    museums = Museum.objects.all()
    return museums
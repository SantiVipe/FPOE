from rest_framework import viewsets
from ..serializers.serializer import ClienteSerializer,ServicioSerializer
from api.models.Modelos import Cliente,Servicio

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
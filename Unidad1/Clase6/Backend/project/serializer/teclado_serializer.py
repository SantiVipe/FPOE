from rest_framework import serializers
from FPOE.Unidad1.Clase6.Backend.api.models.teclado import Teclado
class TecladoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teclado
        
from rest_framework import serializers
from api.models.teclado import Teclado
class TecladoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teclado
        fields = '__all__'

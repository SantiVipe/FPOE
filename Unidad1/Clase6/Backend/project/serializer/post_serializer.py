from rest_framework import serializers
from FPOE.Unidad1.Clase6.Backend.api.models.post import Post
class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post  
        exclude = ['is_removed', 'created', 'modified']

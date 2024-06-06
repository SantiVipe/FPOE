from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializer.teclado_serializer import TecladoSerializers
from api.models.teclado import Teclado
from rest_framework import status
from django.http import Http404
    
class Teclado_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        post = Teclado.objects.all()
        serializer = TecladoSerializers(post, many=True)
        
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = TecladoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Teclado_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Teclado.objects.get(pk=pk)
        except Teclado.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        try:
            teclado = Teclado.objects.get(pk=pk)
        except Teclado.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TecladoSerializers(teclado)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        teclado = self.get_object(pk)
        serializer = TecladoSerializers(teclado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        teclado = self.get_object(pk)
        teclado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

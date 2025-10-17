# views.py

from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils.email import enviar_notificacion

@api_view(['POST'])
def crear_usuario(request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        usuario = serializer.save()
        notificado = enviar_notificacion(usuario.nombre, usuario.email, usuario.telefono)
        return Response({'usuario': serializer.data, 'notificacion_enviada': notificado}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

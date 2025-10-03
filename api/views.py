from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, User 
from .serializers import PostSerializer, UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

@api_view(['POST'])
def user_login(request):
    """
    Login de usuario SEGURO usando la verificación de hash de contraseña de Django.
    """
    user_name = request.data.get('user')
    password = request.data.get('password')

    if not user_name or not password:
        return Response({"error": "Datos incompletos"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user_data = User.objects.get(username=user_name)
    except User.DoesNotExist:
        return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
    
    if user_data.check_password(password):
        
        serializer = UserSerializer(user_data)
        response_data = serializer.data
        response_data.pop('password', None) 
        
        return Response({"user": response_data}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def verify_token(request):
    token = request.data.get('token')

    if token == "tuTokenValido":
        return Response({"valid": True}, status=status.HTTP_200_OK)
    else:
        return Response({"valid": False}, status=status.HTTP_401_UNAUTHORIZED)
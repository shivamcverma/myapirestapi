

from rest_framework import generics
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


from rest_framework_simplejwt.views import TokenObtainPairView

class LoginView(TokenObtainPairView):
    pass
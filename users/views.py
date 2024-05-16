from django.contrib.auth import get_user_model

from .serializers import UserSerializer
from rest_framework import mixins, viewsets, status, generics

from rest_framework.permissions import AllowAny, IsAuthenticated
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

class CreateUserView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
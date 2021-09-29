from rest_framework import viewsets

from user.models import UserModel
from user.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    model = UserModel
    serializer_class = UserSerializer
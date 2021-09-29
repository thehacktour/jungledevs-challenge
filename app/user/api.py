from rest_framework import viewsets

from user.models import UserModel
from user.serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    model = UserModel.objects.all()
    serializer_class = UserSerializer
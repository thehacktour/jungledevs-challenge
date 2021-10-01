from rest_framework import viewsets

from .models import UserModel
from .serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.filter(excluido=False)
    serializer_class = UserSerializer
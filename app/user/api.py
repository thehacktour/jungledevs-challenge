from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import UserModel
from .serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (DjangoModelPermissions,)
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from .models import UserModel
from .serializer import UserSerializer, UserSerializerExpand

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)

    search_fields = (
        "imported_t",
        "status",
        "uuid",
        "username",
    )
    filter_fields = (
        "imported_t",
        "status",
        "uuid",
        "username",
        )
    ordering_fields = (
        "uuid",
    )
    ordering = (
        "uuid",
        "username",
    )

class UserExpandableViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializerExpand
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)

    search_fields = (
        "username",
    )
    filter_fields = (
        "username",
        )
    ordering_fields = (
        "username",
    )
    ordering = (
        "username",
    )

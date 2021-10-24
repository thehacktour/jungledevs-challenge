from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from app.user import mensagens
from rest_framework import status

from .models import UserModel
from .serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)

    search_fields = (
        "username",
    )
    filter_fields = (
        "username",
        )
    ordering_fields = (
        "uuid",
        "points",
    )
    ordering = (
        "uuid",
        "username",
        "points",
    )

    def create(self, request, pk , *args, **kwargs):
        try:
            return super(UserViewSet, self).create(request, *args, **kwargs)
        except KeyError:
            return Response(
                {"non_field_errors": mensagens.MSG_ERRO},
                status=status.HTTP_400_BAD_REQUEST,
            )
    def destroy(self, request, pk, *args, **kwargs):
        try:
            UserModel.objects.filter(id=pk).update()
            return Response({"detail": mensagens.MSG5}, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {"detail": mensagens.MSG_ERRO}, status=status.HTTP_400_BAD_REQUEST
            )

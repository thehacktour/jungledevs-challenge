from rest_framework.routers import DefaultRouter

from user.serializers import UserSerializer

router = DefaultRouter()

router.register('/', UserSerializer, basename='user')

urlpatterns = router.urls
from rest_framework.routers import DefaultRouter

from user.api import UserViewSet

router = DefaultRouter()

router.register('/', UserViewSet, basename='user')

urlpatterns = router.urls
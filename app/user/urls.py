from rest_framework.routers import DefaultRouter

from .api import UserViewSet

router = DefaultRouter()

router.register('user', UserViewSet, basename='user')

urlpatterns = router.urls

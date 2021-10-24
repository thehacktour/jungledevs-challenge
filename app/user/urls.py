from rest_framework.routers import DefaultRouter

from .api import UserViewSet, PointsViewSet

router = DefaultRouter()

router.register('user', UserViewSet, basename='user')
router.register('points', PointsViewSet, basename='user')

urlpatterns = router.urls

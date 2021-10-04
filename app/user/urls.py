from rest_framework.routers import DefaultRouter

from .api import UserViewSet, UserExpandableViewSet

router = DefaultRouter()

router.register('user', UserViewSet, basename='user')
router.register('user-crazy', UserExpandableViewSet, basename='user-crazy')

urlpatterns = router.urls

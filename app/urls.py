from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Fedorov API')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', schema_view),
    path('api/oficial/', include('app.user.urls')),
]

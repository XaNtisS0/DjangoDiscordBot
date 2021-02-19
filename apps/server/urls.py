from django.urls import include, path
from rest_framework import routers

from .views import ServersViewSet


router = routers.SimpleRouter()
router.register('', ServersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import include, path
from rest_framework import routers

from .views import (
    RankViewSet
)

router = routers.DefaultRouter()
router.register(r'', RankViewSet)

urlpatterns = [
    path('', include(router.urls))
]

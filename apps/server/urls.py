from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ServersViewSet, ServersUsersViewSet


router = DefaultRouter()
router.register('', ServersViewSet)
router.register('users', ServersUsersViewSet, basename="users")

urlpatterns = [
    path('', include(router.urls)),
]

import django.urls
from rest_framework_nested import routers

from .views import UsersViewSet


router = routers.SimpleRouter()
router.register('', UsersViewSet)

urlpatterns = [
    django.urls.path('', django.urls.include(router.urls)),
]

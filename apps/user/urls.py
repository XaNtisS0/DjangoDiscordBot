# import django.urls
# from rest_framework_nested import routers

# from .views import UsersViewSet, UserRanksViewSet


# router = routers.SimpleRouter()
# router.register('', UsersViewSet)

# ranks_router = routers.NestedSimpleRouter(router, '', lookup='user')
# ranks_router.register('users', UserRanksViewSet)

# urlpatterns = [
#     django.urls.path('', django.urls.include(router.urls)),
#     django.urls.path('', django.urls.include(ranks_router))
# ]

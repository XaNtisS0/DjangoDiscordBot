# from django.urls import include, path
# from rest_framework_nested import routers
# from rest_framework_nested import routers

# from .views import ServersViewSet, ServerUsersViewSet


# router = routers.SimpleRouter()
# router.register(r'', ServersViewSet)

# users_router = routers.NestedSimpleRouter(router, r'', lookup='user')
# users_router.register(r'users', ServerUsersViewSet, basename='server_users')

# urlpatterns = [
#     path('', include(router.urls)),
#     # path('', include(users_router))
# ]

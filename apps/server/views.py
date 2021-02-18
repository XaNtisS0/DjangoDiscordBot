# from rest_framework import serializers, viewsets
# from rest_framework.response import Response

# from .models import Server
# from ..user.models import User
# from ..user.views import UserSerializer


# class ServerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Server
#         fields = '__all__'


# class ServersViewSet(viewsets.ModelViewSet):
#     serializer_class = ServerSerializer
#     queryset = Server.objects.all()


# class ServerUsersViewSet(viewsets.ViewSet):
#     serializer_class = UserSerializer
#     queryset = Server.objects.all()

#     def list(self, request, server_id):
#         users = User.objects.filter(server=server_id)
#         serializer = self.get_serializer(users, many=True)
#         return Response(serializer.data)

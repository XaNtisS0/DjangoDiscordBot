from rest_framework import serializers, viewsets
from rest_framework.response import Response

from .models import Server
from apps.user.models import User


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'


class ServerUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'
        depth = 1


class ServersViewSet(viewsets.ModelViewSet):
    serializer_class = ServerSerializer
    queryset = Server.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data

        new_server = Server.objects.create(name = data['name'], logging = data['logging'])
        new_server.save()

        for user in data['users']:
            user_obj = User.objects.get(username = user['username'])            
            new_server.users.add(user_obj)
        
        serializer = ServerSerializer(new_server)
            
        return Response(serializer.data)


class ServersUsersViewSet(viewsets.ModelViewSet):
    serializer_class = ServerUsersSerializer
    
    def get_queryset(self):
        servers_with_users = Server.objects.all()
        return servers_with_users
from rest_framework import serializers, viewsets
from rest_framework.response import Response

from .models import User
from apps.rank.models import Rank


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth = 1


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data

        new_user = User.objects.create(username=data['username'])
        new_user.save()

        for rank in data['ranks']:
            try:
                rank_obj = Rank.objects.get(name = rank['name'])
                new_user.ranks.add(rank_obj)
            except Rank.DoesNotExist:
                new_rank = Rank.objects.create(name= rank['name'])
                new_rank.save()
                print(f'rank added with name {rank["name"]}')
                new_user.ranks.add(new_rank)

        serializer = UserSerializer(new_user)

        return Response(serializer.data)

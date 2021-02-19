from rest_framework import viewsets, serializers

from .models import Rank


class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = ['id', 'name']


class RankViewSet(viewsets.ModelViewSet):
    serializer_class = RankSerializer
    queryset = Rank.objects.all()

# from rest_framework import serializers, viewsets
# from rest_framework.response import Response

# from .models import User
# from ..rank.models import Rank


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'


# class UsersViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()


# class UserRanksViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()

#     def list(self, request, user_id):
#         ranks = Rank.objects.filter(users__rank=user_id)
#         serializer = self.get_serializer(ranks, many=True)
#         return Response(serializer.data)

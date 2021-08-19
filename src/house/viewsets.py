import imp
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from house.models import House
from house.serializers import HouseSerializer
from house.permissions import IsHouseManageOrNone

class HouseViewSet(viewsets.ModelViewSet):
  queryset = House.objects.all()
  permission_classes = (IsHouseManageOrNone,)
  serializer_class = HouseSerializer

  @action(detail=True, methods=['post'], name='Join', permission_classes=[])
  def join(self, request, pk=None):
    try:
      house = self.get_object()
      user_profile = request.user.profile
      if (user_profile.house == None):
        user_profile.house = house
        user_profile.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
      elif (user_profile in house.members.all()):
        return Response({'detail': 'Already a member in this house'}, status=status.HTTP_400_BAD_REQUEST)
      else:
        return Response({'detail': 'Already a member in another house'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  
  @action(detail=True, methods=['post'], name='Leave', permission_classes=[])
  def leave(self, request, pk=None):
    try:
      house = self.get_object()
      user_profile = request.user.profile
      if (user_profile.house in house.members.all()):
        user_profile.house = None
        user_profile.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
      else:
        return Response({'detail': 'User not a member in this house'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  @action(detail=True, methods=['post'], name='Remove Member', permission_classes=[])
  def remove_member(self, request, pk=None):
    try:
      house = self.get_object()
      user_id = request.data.get('user_id', None)
      if user_id == None:
        return Response({'user_id': 'Not Provided'}, status=status.HTTP_400_BAD_REQUEST)
      user_profile = User.objects.get(pk=user_id).profile
      house_members = house.members
      if user_profile in house_members.all():
        house_members.remove(user_profile)
        house.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
      else:
        return Response({'detail': 'User not a member in this house'}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist as e:
      return Response({'detail': 'Provided user id does not exist'}, status=status.HTTP_400_BAD_REQUEST)

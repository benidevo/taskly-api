from cgitb import lookup
from email.mime import image
from rest_framework import serializers

from house.models import House

class HouseSerializer(serializers.ModelSerializer):
  members_count = serializers.IntegerField(read_only=True)
  # members = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='profile_detail')
  members = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='profile-detail')

  class Meta:
    model = House
    fields = ['url', 'id', 'image', 'name', 'created_at', 'manager', 'description', 'members_count', 'members', 'points', 'completed_tasks_count', 'uncompleted_tasks_count']
    read_only_fields = ['points', 'completed_tasks_count', 'uncompleted_tasks_count']
    
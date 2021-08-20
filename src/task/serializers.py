from rest_framework import serializers
from task.models import Task, TaskList, Attachment

from house.models import House

class TaskListSerializer(serializers.ModelSerializer):
  house = serializers.HyperlinkedRelatedField(queryset=House.objects.all(), many=False, view_name='house-detail')
  created_by = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name='profile-detail')

  class Meta:
    model = TaskList
    fields =['url', 'id', 'name', 'description', 'status', 'created_on', 'created_by', 'house']
    read_only_fields = ['created_on', 'status']


class TaskSerializer(serializers.ModelSerializer):
  created_by = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name='profile-detail')
  completed_by = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name='profile-detail')
  task_list = serializers.HyperlinkedRelatedField(queryset=TaskList.objects.all(), many=False, view_name='tasklist-detail')
  
  class Meta: 
    model = Task
    fields = ['url', 'id', 'name', 'description', 'status', 'created_on', 'completed_on', 'created_by', 'completed_by', 'task_list']
    read_only_fields = ['created_on', 'completed_on', 'created_by', 'completed_by']


class AttachmentSerializer(serializers.ModelSerializer):
  task = serializers.HyperlinkedRelatedField(queryset=Task.objects.all(), many=False, view_name='task-detail')

  class Meta:
    model = Attachment
    fields = ['url', 'id', 'created_on', 'data', 'task']
    read_only_fields = ['created_on']
    
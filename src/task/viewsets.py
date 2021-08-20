from rest_framework import viewsets, mixins

from task.serializers import AttachmentSerializer, TaskListSerializer, TaskSerializer

from task.models import Task, TaskList, Attachment

from task.permissions import IsAllowedToEditTaskListElseNone, IsAllowedToEditTaskElseNone, IsAllowedToEditAttachmentElseNone

class TaskListViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
  permission_classes = (IsAllowedToEditTaskListElseNone,)
  queryset = TaskList.objects.all()
  serializer_class = TaskListSerializer


class TaskViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAllowedToEditTaskElseNone)
  queryset = Task.objects.all()
  serializer_class = TaskSerializer


class AttachmentViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
  permission_classes = (IsAllowedToEditAttachmentElseNone,)
  queryset = Attachment.objects.all()
  serializer_class = AttachmentSerializer

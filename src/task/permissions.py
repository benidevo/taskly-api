from math import perm
from rest_framework import permissions

class IsAllowedToEditTaskListElseNone(permissions.BasePermission):
  '''
  permission to allow only creator to edit task
  '''

  def has_permission(self, request, view):
    if request.method in permissions.SAFE_METHODS:
      return True
    
    if not request.user.is_anonymous:
      return True
    
    return False

  def has_object_permission(self, request, view, obj):
    return request.user.profile == obj.created_by


class IsAllowedToEditTaskElseNone(permissions.BasePermission):
  '''
  permission to allow only members of a house access to its task
  '''

  def has_permission(self, request, view):
    
    if not request.user.is_anonymous:
      return request.user.profile.house is None
    
    return False

  def has_object_permission(self, request, view, obj):
    return request.user.profile.house == obj.task_list.house

class IsAllowedToEditAttachmentElseNone(permissions.BasePermission):
  '''
  permission to allow only members of a house access to its task
  '''

  def has_permission(self, request, view):
    
    if not request.user.is_anonymous:
      return request.user.profile.house is None
    
    return False

  def has_object_permission(self, request, view, obj):
    return request.user.profile.house == obj.task.task_list

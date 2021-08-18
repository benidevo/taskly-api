from django.contrib.auth.models import User

from rest_framework import viewsets, mixins

from users.models import Profile
from users.serializers import UserSerializer, ProfileSerializer
from users.permissions import IsUserOwnerOrGetAndPostOnly, IsProfileOwnerOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
  permission_classes = (IsUserOwnerOrGetAndPostOnly,)
  queryset = User.objects.all()
  serializer_class = UserSerializer


class ProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
  permission_classes = (IsProfileOwnerOrReadOnly,)
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer

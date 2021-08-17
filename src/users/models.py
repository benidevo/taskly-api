import os

from django.db import models
from django.contrib.auth.models import User

from django.utils.deconstruct import deconstructible


@deconstructible
class GenerateProfileImagePath(object):

    def __init__(self,):
        pass

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        path = f'media/accounts/{instance.user.id}/images'
        name = f'profile_images/.{ext}'
        return os.join(path, name)

profile_image_path = GenerateProfileImagePath()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to=profile_image_path, null=True, blank=True)

    def __str__(self):
        return self.user.username

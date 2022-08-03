from os import O_NDELAY
from django.db import models
from django.contrib.auth.models import User

from common.models import Profile

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=24)


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    content = models.CharField(max_length=128)
    image = models.ImageField(upload_to='likes/', null=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

    

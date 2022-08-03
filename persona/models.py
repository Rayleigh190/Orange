from os import O_NDELAY
from django.db import models
from django.contrib.auth.models import User

from common.models import Profile

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=24)


## 내부 페르소나 모델
class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    content = models.CharField(max_length=128)
    image = models.ImageField(upload_to='likes/', null=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

    
class Strength(models.Model):
    user = user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    content = models.CharField(max_length=128)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)


class Weakness(models.Model):
    user = user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    content = models.CharField(max_length=128)
    hide = models.BooleanField(default=False)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)


class Value(models.Model):
    user = user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    content = models.CharField(max_length=128)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)


## 외부 페르소나 모델
class Solve(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    content = models.CharField(max_length=128)
    image = models.ImageField(upload_to='solve/', null=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from common.models import Profile

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=24)

    def __str__(self):
        return self.tag


class Recommendation(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=64)
    content = models.CharField(max_length=128)

    def __str__(self):
        return self.subject


class HidePersona(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, blank=True)
    HideLikes = models.BooleanField(default=False)
    HideStrength = models.BooleanField(default=False)
    HideWeakness = models.BooleanField(default=False)
    HideValue = models.BooleanField(default=False)
    HideSolve = models.BooleanField(default=False)
    HideCareer = models.BooleanField(default=False)
    HideLiteracy = models.BooleanField(default=False)
    HideLanguage = models.BooleanField(default=False)
    HideMBTI = models.BooleanField(default=False)


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


class Career(models.Model):
    user = user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    content = models.CharField(max_length=128)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)


class Literacy(models.Model):
    user = user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    content = models.CharField(max_length=128)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)


class Language(models.Model):
    user = user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    content = models.CharField(max_length=128)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)


class MBTI(models.Model):
    user = user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    energy = models.IntegerField(default=0, validators=[MinValueValidator(-100), MaxValueValidator(100)])
    recognition = models.IntegerField(default=0, validators=[MinValueValidator(-100), MaxValueValidator(100)])
    judgment = models.IntegerField(default=0, validators=[MinValueValidator(-100), MaxValueValidator(100)])
    lifestyle = models.IntegerField(default=0, validators=[MinValueValidator(-100), MaxValueValidator(100)])
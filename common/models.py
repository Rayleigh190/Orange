from ast import keyword
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nickname = models.CharField(max_length=128)
    introduction = models.CharField(max_length=256, null=True)
    image = models.ImageField(upload_to='profile/', default='default.png')
    follower = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='followings')
    following = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='followers')
    keyword1 = models.CharField(max_length=24, null=True)
    keyword2 = models.CharField(max_length=24, null=True)
    keyword3 = models.CharField(max_length=24, null=True)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
import profile
from pyexpat import model
from typing import List
from rest_framework import serializers

from common.serializers import ProfileSerializer
from .models import Tag, Likes

class LikesSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Likes
        fields = ("pk", "profile", "content", "image", "tag")


class LikesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ("content", "image", "tag")

import profile
from pyexpat import model
from typing import List
from rest_framework import serializers

from common.serializers import ProfileSerializer
from .models import Tag, Likes, Strength, Weakness, Value
from .models import Solve

## 내부 모델 시리얼라이저
class LikesSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Likes
        fields = ("pk", "profile", "content", "image", "tag")


class LikesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ("content", "image", "tag")


class StrengthSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Strength
        fields = ("pk", "profile", "content", "tag")


class StrengthCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strength
        fields = ("content", "tag")


class WeaknessSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Weakness
        fields = ("pk", "profile", "content", "hide", "tag")


class WeaknessCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weakness
        fields = ("content", "hide", "tag")


class ValueSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Value
        fields = ("pk", "profile", "content", "tag")


class ValueCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ("content", "tag")


## 외부 모델 시리얼라이저
class SolveSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Solve
        fields = ("pk", "profile", "content", "image", "tag")


class SolveCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solve
        fields = ("content", "image", "tag")
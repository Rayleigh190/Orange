from rest_framework import serializers

from common.serializers import ProfileSerializer
from .models import Recommendation, HidePersona
from .models import Tag, Likes, Strength, Weakness, Value
from .models import Solve, Career, Literacy, Language, MBTI

## 테그 모델 시리얼 라이저
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("pk", "tag")


class TagCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("tag")


## 프리즘 모델 시리얼라이저
class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = ("pk", "tag", "subject", "content")


class RecommendationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = ("tag", "subject", "content")


class HidePersonaSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = HidePersona
        fields = ("pk", "profile", "HideLikes", "HideStrength", "HideWeakness", "HideValue", "HideSolve", "HideCareer", "HideLiteracy", "HideLanguage", "HideMBTI")


class HidePersonaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HidePersona
        fields = ("HideLikes", "HideStrength", "HideWeakness", "HideValue", "HideSolve", "HideCareer", "HideLiteracy", "HideLanguage", "HideMBTI")


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
        fields = ("pk", "profile", "content", "tag")


class WeaknessCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weakness
        fields = ("content", "tag")


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


class CareerSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Career
        fields = ("pk", "profile", "content", "tag")


class CareerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ("content", "tag")


class LiteracySerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Literacy
        fields = ("pk", "profile", "content", "tag")


class LiteracyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Literacy
        fields = ("content", "tag")


class LanguageSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Language
        fields = ("pk", "profile", "content", "tag")


class LanguageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ("content", "tag")


class MBTISerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = MBTI
        fields = ("pk", "profile", "energy", "recognition", "judgment", "lifestyle")


class MBTICreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MBTI
        fields = ("energy", "recognition", "judgment", "lifestyle")
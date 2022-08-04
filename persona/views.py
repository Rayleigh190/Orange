import profile
from django.shortcuts import render
from rest_framework import viewsets

from common.models import Profile
from .models import Likes, Strength, Weakness, Value
from .models import Solve, Career, Literacy, Language
from .permissions import CustomReadOnly
from .serializers import LikesSerializer, LikesCreateSerializer
from .serializers import StrengthSerializer, StrengthCreateSerializer
from .serializers import WeaknessSerializer, WeaknessCreateSerializer
from .serializers import ValueSerializer, ValueCreateSerializer
from .serializers import SolveSerializer, SolveCreateSerializer
from .serializers import CareerSerializer, CareerCreateSerializer
from .serializers import LiteracySerializer, LiteracyCreateSerializer
from .serializers import LanguageSerializer, LanguageCreateSerializer

# Create your views here.
## 내부 뷰셋
class LikesViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return LikesSerializer
        return LikesCreateSerializer
    
    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(user=self.request.user, profile=profile)


class StrengthViewSet(viewsets.ModelViewSet):
    queryset = Strength.objects.all()
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return StrengthSerializer
        return StrengthCreateSerializer
    
    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(user=self.request.user, profile=profile)


class WeaknessViewSet(viewsets.ModelViewSet):
    queryset = Weakness.objects.all()
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return WeaknessSerializer
        return WeaknessCreateSerializer
    
    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(user=self.request.user, profile=profile)


class ValueViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return ValueSerializer
        return ValueCreateSerializer
    
    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(user=self.request.user, profile=profile)


## 외부 뷰셋
class SolveViewSet(viewsets.ModelViewSet):
    queryset = Solve.objects.all()
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return SolveSerializer
        return SolveCreateSerializer
    
    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(user=self.request.user, profile=profile)


class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return CareerSerializer
        return CareerCreateSerializer
    
    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(user=self.request.user, profile=profile)


class LiteracyViewSet(viewsets.ModelViewSet):
    queryset = Literacy.objects.all()
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return LiteracySerializer
        return LiteracyCreateSerializer
    
    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(user=self.request.user, profile=profile)


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return LanguageSerializer
        return LanguageCreateSerializer
    
    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(user=self.request.user, profile=profile)
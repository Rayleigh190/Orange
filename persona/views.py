import profile
from django.shortcuts import render
from rest_framework import viewsets

from common.models import Profile
from .models import Likes
from .permissions import CustomReadOnly
from .serializers import LikesSerializer, LikesCreateSerializer

# Create your views here.
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
    

import imp
from operator import imod
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer, FollowSerializer
from .models import Profile
from .permissions import CustomReadOnly

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"token": token.key}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [CustomReadOnly]


# 팔로우 기능
# following : 유저가 팔로우 한 다른 유저(유저가 친구로 추가한 사람들)
# follower: 유저를 팔로우 한 다른 유저 (유저를 친구로 추가한 사람들)

class FollowUser(APIView):
    def post(self, request, pk, format=None):
        user = request.user
        profile = Profile.objects.get(user=user)
        try:
            user_to_follow = Profile.objects.get(user=pk)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        profile.following.add(user_to_follow)
        user_to_follow.follower.add(profile)
        return Response(status=status.HTTP_200_OK)


class UnfollowUser(APIView):
    def post(self, request, pk, format=None):
        user = request.user
        profile = Profile.objects.get(user=user)
        try:
            user_to_unfollow = Profile.objects.get(user=pk)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        profile.following.remove(user_to_unfollow)
        user_to_unfollow.follower.remove(profile)
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def ShowFollowing(request, pk):
    profile = Profile.objects.filter(follower=pk)
    serializer = FollowSerializer(profile, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def ShowFollower(request, pk):
    profile = Profile.objects.filter(following=pk)
    serializer = FollowSerializer(profile, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
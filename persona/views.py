import random
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from common.models import Profile
from .models import Recommendation
from .models import Likes, Strength, Weakness, Value
from .models import Solve, Career, Literacy, Language, MBTI
from .permissions import CustomReadOnly
from .serializers import RecommendationSerializer, RecommendationCreateSerializer
from .serializers import LikesSerializer, LikesCreateSerializer
from .serializers import StrengthSerializer, StrengthCreateSerializer
from .serializers import WeaknessSerializer, WeaknessCreateSerializer
from .serializers import ValueSerializer, ValueCreateSerializer
from .serializers import SolveSerializer, SolveCreateSerializer
from .serializers import CareerSerializer, CareerCreateSerializer
from .serializers import LiteracySerializer, LiteracyCreateSerializer
from .serializers import LanguageSerializer, LanguageCreateSerializer
from .serializers import MBTISerializer, MBTICreateSerializer

# 각 게시물 리스트에서 tag만 추출하는 함수
def GetTag(MyList1, MyList2, MyList3, MyList4):
    MyLists = [MyList1, MyList2, MyList3, MyList4]
    TagList = []
    for MyList in MyLists:
        for value in MyList:
                tag = value.tag
                TagList.append(tag)
    return TagList

# Create your views here.
## 프리즘 뷰
class InnerRecommendationAPI(APIView): # 내부 페르소나 관련 추천 게시물을 보내주는 뷰
    def get(self, request):
        # 각 inner 모델에서 사용자의 게시물 가져오기
        MyLikesList = Likes.objects.filter(user=request.user)
        MyStrengthList = Strength.objects.filter(user=request.user)
        MyWeaknessList = Weakness.objects.filter(user=request.user)
        MyValueList = Value.objects.filter(user=request.user)
        TagList = GetTag(list(MyLikesList), list(MyStrengthList), list(MyWeaknessList), list(MyValueList)) # tag만 추출
        my_set = set(TagList) # 집합set으로 변환 -> 중복 제거
        TagList = list(my_set) # list로 재변환
        random.shuffle(TagList) # tag 랜덤으로 섞기
        RecommendationList = Recommendation.objects.none() # 빈 쿼리셋
        for MyTag in TagList[:4]: # TagList의 상위 4개 태그에 대해서만 추천 게시물 선택
            object_list = Recommendation.objects.filter(tag=MyTag) # MyTag를 가진 모든 추천 게시물을 가져옴
            pk_list = [] # object_list에 가져온 추천 게시물들의 pk를 저장할 빈 리스트
            for object in object_list: # object_list의 각 object에서 pk만 추출
                pk_list.append(object.pk)
            recommendation = Recommendation.objects.filter(pk=random.choice(pk_list)) # pk_list에서 pk를 랜덤으로 하나 선택해서 추천 게시물 선택
            RecommendationList = RecommendationList.union(recommendation) # 빈 쿼리셋에 넣기
        serializer = RecommendationSerializer(RecommendationList, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OuterRecommendationAPI(APIView): # 외부 페르소나 관련 추천 게시물을 보내주는 뷰
    def get(self, request):
        # 각 outer 모델에서 사용자의 게시물 가져오기
        MySolveList = Solve.objects.filter(user=request.user)
        MyCareerList = Career.objects.filter(user=request.user)
        MyLiteracyList = Literacy.objects.filter(user=request.user)
        MyLanguageList = Language.objects.filter(user=request.user)
        TagList = GetTag(list(MySolveList), list(MyCareerList), list(MyLiteracyList), list(MyLanguageList)) # tag만 추출
        my_set = set(TagList) # 집합set으로 변환 -> 중복 제거
        TagList = list(my_set) # list로 재변환
        random.shuffle(TagList) # tag 랜덤으로 섞기
        RecommendationList = Recommendation.objects.none() # 빈 쿼리셋
        for MyTag in TagList[:4]: # TagList의 상위 4개 태그에 대해서만 추천 게시물 선택
            object_list = Recommendation.objects.filter(tag=MyTag) # MyTag를 가진 모든 추천 게시물을 가져옴
            pk_list = [] # object_list에 가져온 추천 게시물들의 pk를 저장할 빈 리스트
            for object in object_list: # object_list의 각 object에서 pk만 추출
                pk_list.append(object.pk)
            recommendation = Recommendation.objects.filter(pk=random.choice(pk_list)) # pk_list에서 pk를 랜덤으로 하나 선택해서 추천 게시물 선택
            RecommendationList = RecommendationList.union(recommendation) # 빈 쿼리셋에 넣기
        serializer = RecommendationSerializer(RecommendationList, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return RecommendationSerializer
        return RecommendationCreateSerializer


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


class MBTIViewSet(viewsets.ModelViewSet):
    queryset = MBTI.objects.all()
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return MBTISerializer
        return MBTICreateSerializer
    
    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(user=self.request.user, profile=profile)
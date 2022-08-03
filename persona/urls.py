from django.urls import path
from rest_framework import routers

from .views import LikesViewSet

router = routers.SimpleRouter()
router.register('likes', LikesViewSet)

urlpatterns = router.urls
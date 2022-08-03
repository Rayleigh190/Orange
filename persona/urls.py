from django.urls import path
from rest_framework import routers

from .views import LikesViewSet, StrengthViewSet, WeaknessViewSet

router = routers.SimpleRouter()
router.register('likes', LikesViewSet)
router.register('strength', StrengthViewSet)
router.register('weakness', WeaknessViewSet)

urlpatterns = router.urls
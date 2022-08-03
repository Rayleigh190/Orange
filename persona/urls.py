from django.urls import path
from rest_framework import routers

from .views import LikesViewSet, StrengthViewSet, WeaknessViewSet, ValueViewSet

router = routers.SimpleRouter()
router.register('likes', LikesViewSet)
router.register('strength', StrengthViewSet)
router.register('weakness', WeaknessViewSet)
router.register('value', ValueViewSet)

urlpatterns = router.urls
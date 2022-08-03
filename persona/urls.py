from django.urls import path
from rest_framework import routers

from .views import LikesViewSet, StrengthViewSet, WeaknessViewSet, ValueViewSet
from .views import SolveViewSet

router = routers.SimpleRouter()
## 내부 inner/
router.register('likes', LikesViewSet)
router.register('strength', StrengthViewSet)
router.register('weakness', WeaknessViewSet)
router.register('value', ValueViewSet)
## 외부, outer/
router.register('solve', SolveViewSet)

urlpatterns = router.urls
from django.urls import path
from rest_framework import routers

from .views import LikesViewSet, StrengthViewSet, WeaknessViewSet, ValueViewSet
from .views import SolveViewSet, CareerViewSet

router = routers.SimpleRouter()
## 내부 inner/
router.register('likes', LikesViewSet)
router.register('strength', StrengthViewSet)
router.register('weakness', WeaknessViewSet)
router.register('value', ValueViewSet)
## 외부, outer/
router.register('solve', SolveViewSet)
router.register('career', CareerViewSet)

urlpatterns = router.urls
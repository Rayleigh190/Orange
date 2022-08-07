from django.urls import path
from .views import RegisterView, LoginView, ProfileView, LogoutView
from .views import FollowUser, UnfollowUser, ShowFollowing, ShowFollower

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('profile/<int:pk>/', ProfileView.as_view()),
    path('<int:pk>/follow/', FollowUser.as_view()),
    path('<int:pk>/unfollow/', UnfollowUser.as_view()),
    path('<int:pk>/following/', ShowFollowing),
    path('<int:pk>/follower/', ShowFollower),
]
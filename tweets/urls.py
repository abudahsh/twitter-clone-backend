from django.urls import path, include

from rest_framework import routers
from .views import TweetViewSet, ProfileTweets


router = routers.DefaultRouter()
router.register('tweets', TweetViewSet, base_name="tweets")

urlpatterns = [
    path("", include(router.urls)),
    path('pro/<int:profile>/', ProfileTweets.as_view(), name="protweets")
]

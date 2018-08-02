from django.urls import path, include

from rest_framework import routers
from .views import TweetViewSet


router = routers.DefaultRouter()
router.register('tweets', TweetViewSet, base_name="tweets")


urlpatterns = [
    path("", include(router.urls)),
]

from rest_framework import viewsets, permissions, generics

from profiles.models import Profile
from .models import Tweet
from .serializers import TweetSerializer
# Create your views here.


class TweetViewSet(viewsets.ModelViewSet):

    serializer_class = TweetSerializer

    def get_queryset(self):
        return Tweet.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.profile)


class ProfileTweets(generics.ListAPIView):
    serializer_class = TweetSerializer

    def get_queryset(self):
        pk=self.kwargs['profile']
        profile=Profile.objects.get(pk=pk)
        return Tweet.objects.filter(created_by=profile)
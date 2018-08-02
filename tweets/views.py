from rest_framework import viewsets, permissions
from .models import Tweet
from .serializers import TweetSerializer
# Create your views here.


class TweetViewSet(viewsets.ModelViewSet):

    serializer_class = TweetSerializer

    def get_queryset(self):
        return Tweet.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.profile)

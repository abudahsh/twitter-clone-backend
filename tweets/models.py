from django.db import models

# Create your models here.
from profiles.models import Profile


class Tweet(models.Model):
    created_by=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tweets')
    body=models.TextField(max_length=300)
    media=models.URLField(null=True, blank=True, )
    is_liked=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body

class ReTweet(Tweet):

    origin_tweet=models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='retweets')



class Reply(Tweet):

    reply_on=models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='replies', verbose_name='replies')

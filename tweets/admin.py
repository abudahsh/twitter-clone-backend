from django.contrib import admin

from .models import Tweet, Reply, ReTweet
# Register your models here.
admin.site.register(Tweet)
admin.site.register(Reply)
admin.site.register(ReTweet)

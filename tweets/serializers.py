from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.ModelSerializer):
    creator = serializers.SerializerMethodField(read_only=True)
    nick_name= serializers.SerializerMethodField(read_only=True)
    profile_pic = serializers.SerializerMethodField(read_only=True)
    def get_creator(self, obj):
        return obj.created_by.username
    def get_nick_name(self, obj):
        return obj.created_by.nickname  
    def get_profile_pic(self, obj):
        """Gets the picture's url then append it to the localhost ip to give absolute url"""
        request = self.context.get('request')
        return request.build_absolute_uri(obj.created_by.picture.url)
    class Meta:
        model = Tweet
        fields=['id','creator', 'nick_name','profile_pic','body', 'media', 'created_at']
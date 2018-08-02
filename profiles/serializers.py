from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile


class ProfileSerializer (serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [ 'username', 'nickname', 'bio', 'picture']

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['id', 'username', 'email', 'is_staff']



class CreateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False, allow_null=True)
    class Meta:
        model = User
        fields = ('id', 'username',  'email','password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        None,
                                        validated_data['password'])
        return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")



class DumbTestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")
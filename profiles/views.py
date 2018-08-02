from django.contrib.auth import  login
from django.contrib.auth.models import User
from knox.auth import TokenAuthentication
from knox.models import AuthToken

from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from braces.views import CsrfExemptMixin
from .serializers import UserSerializer, CreateUserSerializer, LoginUserSerializer, ProfileSerializer


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegistrationAPI(CsrfExemptMixin, generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })


class LoginAPI(CsrfExemptMixin, generics.GenericAPIView):
    
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user),
            'profile':ProfileSerializer(user.profile, context=self.get_serializer_context()).data
        })


class UserAPI(CsrfExemptMixin, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

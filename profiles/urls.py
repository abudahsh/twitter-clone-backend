from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, RegistrationAPI, LoginAPI, UserAPI

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)



urlpatterns = [
    path(r'api/', include(router.urls)),
    path("auth/register/", RegistrationAPI.as_view(),name='register'),
    path("auth/login/", LoginAPI.as_view(), name='login'),
    path("auth/user/", UserAPI.as_view(), name='current_user'),
    path('api-auth/', include('rest_framework.urls'))

]

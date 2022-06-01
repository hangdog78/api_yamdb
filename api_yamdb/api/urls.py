from django.urls import include, path
from rest_framework import routers
from .views import (UserViewSet,
                    signup_post,
                    token_post)

api_v1_router = routers.DefaultRouter()
api_v1_router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/auth/token/', token_post),
    path('v1/auth/signup/', signup_post),
    path('v1/', include(api_v1_router.urls)),
]

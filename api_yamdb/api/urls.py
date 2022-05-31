from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet

api_v1_router = routers.DefaultRouter()
api_v1_router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(api_v1_router.urls)),
]
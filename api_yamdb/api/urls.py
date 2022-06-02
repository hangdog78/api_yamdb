from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (CategoryViewSet,
                    TitleViewSet,
                    GenreViewSet,
                    UserViewSet,
                    signup_post,
                    token_post)

api_v1_router = DefaultRouter()
api_v1_router.register('users', UserViewSet, basename='users')
api_v1_router.register(r'titles', TitleViewSet, basename='title')
api_v1_router.register(r'categories', CategoryViewSet, basename='category')
api_v1_router.register(r'genres', GenreViewSet, basename='genre')

urlpatterns = [
    path('v1/auth/token/', token_post),
    path('v1/auth/signup/', signup_post),
    path('v1/', include(api_v1_router.urls))
]

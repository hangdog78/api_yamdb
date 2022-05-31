from rest_framework import filters, permissions, viewsets

from .permissions import AdminPermission
from .serializers import UserSerializer
from users.models import User


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (AdminPermission,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


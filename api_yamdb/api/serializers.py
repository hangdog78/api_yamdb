from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User


class UserSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = User
        fields = '__all__'
        
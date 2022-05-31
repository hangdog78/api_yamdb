from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User


class UserSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'email': {
                'validators': [
                    UniqueValidator(
                        queryset=User.objects.all()
                        )
                    ]
                },
            'username': {
                'validators': [
                    UniqueValidator(
                        queryset=User.objects.all()
                        )
                    ]
                }
            
            }
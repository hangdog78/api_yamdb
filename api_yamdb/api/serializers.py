from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    '''Сериализация данных пользователя'''
  
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'bio',
                  'role')
        
        
class MeSerializer(serializers.ModelSerializer):
    '''Сериализация данных пользователя для эндпоинта me'''
    role = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'bio',
                  'role')

class SignUpSerializer(serializers.Serializer):
    '''Сериализация для регистрации пользователя'''
    email = serializers.EmailField(max_length=254, required=True)
    username = serializers.CharField(max_length=150, required=True)
    
    def validate(self, data):
        if data['username'] == 'me':
            raise serializers.ValidationError('Login -me- is prohibited.')
        return data

    class Meta:
        fields = ('username', 'email')

        
class TokenSerializer(serializers.Serializer):
    '''Сериализация для выдачи токена'''
    username = serializers.CharField(max_length=150, required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        fields = ('username', 'confirmation_code')
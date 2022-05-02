from rest_framework import serializers
from .models import *


class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'full_name',
            'email',
            'password',
            'password2'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password must be the same!")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'full_name', 'email']


class EditUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['id', 'full_name', 'email']
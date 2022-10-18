from clubs.models import Club
from rest_framework import serializers
from .models import User

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class ClubUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Club
        fields = '__all__'

from django.conf.global_settings import AUTH_USER_MODEL
from rest_framework import serializers, permissions
from rest_framework.authtoken.admin import User
from rest_framework.views import APIView

from .models import Videogame, Partia, Chat, Partia_User, User_profile


class VideogameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Videogame
        #fields = '__all__'
        fields = ('name', 'description')


class PartiaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partia
        fields = ('name', 'description', 'created_date', 'creator', 'videogame')
        #fields = '__all__'

class PartiaUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partia_User
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = '__all__'

class PartiaVGSerializer (serializers.ModelSerializer):

    class Meta:
        model = Partia
        fields = '__all__'

class UserProfileSerializer (serializers.ModelSerializer):

    class Meta:
        model = User_profile
        fields = '__all__'

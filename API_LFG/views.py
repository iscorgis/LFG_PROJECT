from django.contrib.auth import logout
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from rest_framework import viewsets, generics, status, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import VideogameSerializer
from .serializers import ChatSerializer
from .serializers import PartiaSerializer
from .serializers import PartiaUserSerializer,PartiaVGSerializer, UserProfileSerializer

from .models import Videogame, Chat, Partia, Partia_User, User_profile

from rest_framework.decorators import api_view, permission_classes, renderer_classes, authentication_classes, action
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

class VideoGameViewSet(viewsets.ModelViewSet):
        queryset = Videogame.objects.all().order_by('name')
        serializer_class = VideogameSerializer

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all().order_by('chat_name')
    serializer_class = ChatSerializer

class PartiaViewSet(viewsets.ModelViewSet):
    serializer_class = PartiaSerializer

    #def get_queryset(self):
    #    return Partia.objects.filter(videogame=1)
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Partia.objects.all()
        vd = self.request.query_params.get('vd')
        print(self.request.query_params.getlist('vd'))
        if vd is not None:
            queryset = queryset.filter(videogame=vd)
        return queryset
        #http://127.0.0.1:8000/partia/?vd=1


class PartiaUserViewSet(viewsets.ModelViewSet):

    http_method_names = ["get","post", "delete"]
    #queryset = Partia_User.objects.all()
    serializer_class = PartiaUserSerializer
    #permission_classes = (permissions.IsAuthenticated)

    def get_queryset(self):
        queryset = Partia_User.objects.all()
        id_user = self.request.user
        id_partia = self.request.query_params.get('id_partia')
        if id_partia is not None:
            queryset = queryset.filter(id_partia=id_partia, id_user=id_user)
            return queryset
"""
    def perform_create(self, serializer):
        serializer.save(id_user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
"""
class PartiaUserGetInViewSet(viewsets.ModelViewSet):

    http_method_names = ["post"]
    #queryset = Partia_User.objects.all()
    serializer_class = PartiaUserSerializer
    permission_classes = (permissions.IsAuthenticated)

'''
class x(viewsets.ModelViewSet):
    queryset = Partia_User.objects.all()
    serializer_class = PartiaUserSerializer

    def destroy(self, request, *args, **kwargs):
        pu = self.get_object()
        #doctor.is_active = False
        #doctor.save()
        return Response(data='delete success')
'''

class PartiaUserGetOutViewSet(viewsets.ModelViewSet):

    http_method_names = ["delete"]
    #queryset = Partia_User.objects.all()
    serializer_class = PartiaUserSerializer
    permission_classes = (permissions.IsAuthenticated)

    def get_queryset(self):
        queryset = Partia_User.objects.all()
        id_user = self.request.user
        id_partia = self.request.query_params.get('id_partia')
        if id_partia is not None:
            queryset = queryset.filter(id_partia=id_partia, id_user=id_user)
            return queryset


class ChatListViewSet(viewsets.ModelViewSet):

    http_method_names = ["get"]
    serializer_class = ChatSerializer
    #permission_classes = permissions.IsAuthenticated

    #Sobreescribimos el metodo std para filtrar solo los msg de una determinada sala de chat
    def get_queryset(self):
        queryset = Chat.objects.all()
        id_partia = self.request.query_params.get('id_partia')
        if id_partia is not None:
            queryset = queryset.filter(partia=id_partia)
            return queryset
            #http://127.0.0.1:8000/chatlist/?id_partia=1

class ChatSendMsgViewSet(viewsets.ModelViewSet):
    #curl -X POST -d "comment=a&partia=1&user=1"  http://127.0.0.1:8000/SendChatMsg/

    http_method_names = ["post"]
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        request = serializer.context['request']
        serializer.save(user = self.request.user)

    #def create(self, request, *args, **kwargs):

        #chat_message = self.get_object()
        #chat_message.partia = request.data['partia']
        #chat_message.user = request.data['user']
        #chat_message.comment = request.data['comment']
        #chat_message.save()

        #print(request.data['partia'])
        #print(request.data['user'])
        #print(request.data['comment'])
        #print(args)
        #print(kwargs) - es para el queryset
        #return Response(data='create success')
        #request.data['user'] = 2
        #return super(ChatSendMsgViewSet, self).create(request, *args, **kwargs)

class ChatEditMsgViewSet(viewsets.ModelViewSet):
    #http://127.0.0.1:8000/ChatEditMsg/?id=1
    http_method_names   = ["get","put","delete"]
    queryset            = Chat.objects.all()
    serializer_class    = ChatSerializer
    #permission_classes  = permissions.IsAuthenticated

    def get_queryset(self):
        queryset = Chat.objects.all()
        user_id = self.request.user
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(id=id, user_id=user_id)
        return queryset

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class    = UserProfileSerializer

    def get_queryset(self):
        """
        Filter the queryset with the logged user
        """
        user = self.request.user
        return User_profile.objects.filter(user=user)

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


# Authentication by session or basic http
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes([IsAuthenticated])
class VideoGameViewSet(viewsets.ModelViewSet):

        """View Used to store the VideoGame data that will be used to create partias/groups"""
        queryset = Videogame.objects.all().order_by('name')
        serializer_class = VideogameSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all().order_by('chat_name')
    serializer_class = ChatSerializer

@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes([IsAuthenticated])
class PartiaViewSet(viewsets.ModelViewSet):

    """View uset to create Partias/Groups"""
    http_method_names = ["get", "post"]
    serializer_class = PartiaSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned partias to a given videogame,
        by filtering against a `videogame` query parameter in the URL.
        """
        queryset = Partia.objects.all()
        vd = self.request.query_params.get('vd')
        if vd is not None:
            queryset = queryset.filter(videogame=vd)
        return queryset
        #http://127.0.0.1:8000/partia/?vd=1


@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes([IsAuthenticated])
class PartiaUserViewSet(viewsets.ModelViewSet):

    """ View used by users to get in/out from partias/groups"""
    http_method_names = ["post", "delete"]
    serializer_class = PartiaUserSerializer

    def get_queryset(self):
        queryset = Partia_User.objects.all().filter(id_user=self.request.user)
        id_partia = self.request.query_params.get('id_partia')
        if id_partia is not None:
            queryset = queryset.filter(id_partia=id_partia)
        return queryset


@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes([IsAuthenticated])
class ChatListViewSet(viewsets.ModelViewSet):

    http_method_names = ["get"]
    serializer_class = ChatSerializer

    """Overwrite the standard method to filter de objets by partia id"""
    def get_queryset(self):
        queryset = Chat.objects.all()
        id_partia = self.request.query_params.get('id_partia')
        if id_partia is not None:
            queryset = queryset.filter(partia=id_partia)
            return queryset

@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes([IsAuthenticated])
class ChatSendMsgViewSet(viewsets.ModelViewSet):

    """View used to send messages by the logged user to the party/group"""
    http_method_names = ["post"]
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        request = serializer.context['request']
        serializer.save(user = self.request.user)

@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes([IsAuthenticated])
class ChatEditMsgViewSet(viewsets.ModelViewSet):

    """View Used for Update or Delete messages that the logged user send to the party/group"""
    http_method_names   = ["get", "put", "delete"]
    queryset            = Chat.objects.all()
    serializer_class    = ChatSerializer

    def get_queryset(self):
        queryset = Chat.objects.all().filter(user_id = self.request.user)
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset

@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes([IsAuthenticated])
class UserProfileViewSet(viewsets.ModelViewSet):

    """View used for CRUD operations over user private profile"""
    serializer_class    = UserProfileSerializer
    def get_queryset(self):
        """
        Filter the queryset with the logged user
        """
        user = self.request.user
        return User_profile.objects.filter(user=user)

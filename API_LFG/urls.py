
from django.urls import include, path
from rest_framework import routers
from API_LFG import views

router = routers.DefaultRouter()
router.register(r'videogame', views.VideoGameViewSet, 'videogame')
router.register(r'partia', views.PartiaViewSet, 'partia')
#router.register(r'chatlist', views.ChatViewSet, 'chat')
router.register(r'partia_user', views.PartiaUserViewSet, 'partia_user')
#router.register(r'get_in', views.PartiaUserGetInViewSet, 'get_out')
#router.register(r'get_out', views.PartiaUserGetOutViewSet, 'get_in')
router.register(r'ChatEditMsg', views.ChatEditMsgViewSet)
router.register(r'chatlist', views.ChatListViewSet, 'chatlist')
router.register(r'SendChatMsg', views.ChatSendMsgViewSet, 'SendChatMsg')
router.register(r'UserProfile', views.UserProfileViewSet, 'UserProfile')

#router.register(r'find', views.FindPartiaByVideoGame, basename='abc')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    #path('api/welcome', views.welcome )
]   
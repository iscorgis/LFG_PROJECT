
from django.urls import include, path
from rest_framework import routers
from API_LFG import views

router = routers.DefaultRouter()
router.register(r'videogame',   views.VideoGameViewSet,     'videogame')    #ALL CRUD OPERATIONS
router.register(r'partia',      views.PartiaViewSet,        'partia')       #GET/POST
router.register(r'partia_user', views.PartiaUserViewSet,    'partia_user')  #POST/DELETE
router.register(r'ChatEditMsg', views.ChatEditMsgViewSet,   'ChatEditMsg')  #GET/PUT/DELETE
router.register(r'chatlist',    views.ChatListViewSet,      'chatlist')     #GET
router.register(r'SendChatMsg', views.ChatSendMsgViewSet,   'SendChatMsg')  #POST
router.register(r'UserProfile', views.UserProfileViewSet,   'UserProfile')  #ALL CRUD OPERATIONS

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('registration/', include('rest_auth.registration.urls'))
    #path('api/welcome', views.welcome )
]   
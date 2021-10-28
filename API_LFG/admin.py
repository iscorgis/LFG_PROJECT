from django.contrib import admin

from .models         import Videogame, Partia, Chat, Partia_User, User_profile

# Register your models here.
admin.site.register(Videogame)
admin.site.register(Partia)
admin.site.register(Chat)
admin.site.register(Partia_User)
admin.site.register(User_profile)


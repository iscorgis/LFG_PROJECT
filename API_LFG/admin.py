from django.contrib import admin

from .models         import Videogame
from .models         import Partia
from .models         import Chat
from .models         import Partia_User

# Register your models here.
admin.site.register(Videogame)
admin.site.register(Partia)
admin.site.register(Chat)
admin.site.register(Partia_User)

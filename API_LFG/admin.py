from django.contrib import admin
from .models         import Videogame
from .models         import Partia
from .models         import Chat

# Register your models here.
admin.site.register(Videogame)
admin.site.register(Partia)
admin.site.register(Chat)
from django.conf import settings
from django.db import models
from django.utils import timezone
import random

def random_string():
    return str(random.randint(10000, 99999))

class Videogame(models.Model):
    name            = models.CharField(max_length=50)
    description     = models.CharField(max_length=300)
    created_date    = models.DateTimeField(default=timezone.now)
    active          = models.BooleanField(default=True)


class Partia(models.Model):
    name            = models.CharField(max_length=50)
    description     = models.CharField(max_length=300)
    created_date    = models.DateTimeField(default=timezone.now)
    creator         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    videogame       = models.ForeignKey(Videogame,on_delete=models.CASCADE)

#Loged Users in a Partia
class Partia_User(models.Model):
    id_partia     = models.ForeignKey(Partia,on_delete=models.CASCADE)
    id_user       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )

#Model to save the message data send by users
class Chat(models.Model):
    partia          = models.ForeignKey(Partia,on_delete=models.CASCADE)
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chat_name       = models.CharField(max_length=50, default=random_string)
    comment         = models.CharField(max_length=300)

#Model to store profile user data




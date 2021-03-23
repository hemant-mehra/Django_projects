from django.db import models
# inbuild user model
from django.contrib import auth
# Create your models here.

# using inbuid models for usr
class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return '@{}'.format(self.username) #username is defined in inbuit model

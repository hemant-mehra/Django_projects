from django.contrib import admin
from . import models
# Register your models here.
# check out udemy notes i created
class GroupMemberInline(admin.TabularInline):
    model= models.GroupMember
admin.site.register(models.Group)

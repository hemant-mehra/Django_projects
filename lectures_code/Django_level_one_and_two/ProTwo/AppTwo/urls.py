from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from AppTwo import views

urlpatterns = [
    url(r"^$",views.index,name="index"),
    url(r"^$",views.user_func,name="user_func")
]

from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from AppTwo import views

urlpatterns = [
    url(r"^$",views.index,name="index"),
    url(r"^$",views.form_name_view,name="user_func")
]

"""ProTwo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from AppTwo import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^help",include("AppTwo.urls")),
    url(r"^$",views.index,name="index"),
    # url(r"^users/",views.user_func,name='user_func')
    url(r"^users/",views.form_name_view,name="user_func"),
]

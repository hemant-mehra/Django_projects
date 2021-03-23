from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.
def index(request):
    my_dir={"help_me":"Help Page"}
    return render(request,"AppTwo/help.html",context=my_dir)

def user_func(request):
    name_list=User.objects.order_by("id")
    name_dict={"name_records":name_list}
    return render(request,"AppTwo/user_func.html",context=name_dict)

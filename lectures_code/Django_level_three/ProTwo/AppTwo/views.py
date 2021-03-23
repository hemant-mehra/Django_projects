from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo import forms
# Create your views here.
def index(request):
    my_dir={"help_me":"Help Page"}
    return render(request,"AppTwo/help.html",context=my_dir)

# def user_func(request):
#     name_list=User.objects.order_by("id")
#     name_dict={"name_records":name_list}
#     return render(request,"AppTwo/user_func.html",context=name_dict)


def form_name_view(request):
    form=forms.MyNewForm()
    if request.method=="POST":
        form=forms.MyNewForm(request.POST)

        if form.is_valid():
            ## do something code
            new_user = form.save()
    return render(request,"AppTwo/user_func.html",{"form":form})

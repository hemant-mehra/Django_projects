from django.shortcuts import render
from basicapp import forms
# or could use
# from . import forms


# Create your views here.
def index(request):
    return render(request,"basicapp/index.html")

def form_name_view(request):
    form=forms.FormName()
    if request.method=="POST":
        form=forms.FormName(request.POST)

        if form.is_valid():
            ## do something code
            print("validation sucess!")
            print("name : "+form.cleaned_data["name"])
            print("Email: " +form.cleaned_data["email"])
            print("Tex: "+ form.cleaned_data["text"])
    return render(request,"basicapp/form_page.html",{"form":form})

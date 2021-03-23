from django.shortcuts import render
from django.http import HttpResponse
# connecting to database
from first_app.models import Topic,AccessRecord,Webpage
# Create your views here.
def index(request):
    webpages_list=AccessRecord.objects.order_by("name")
    date_dict={"access_records":webpages_list}
    # my_dict={"insert_me":"Hello i am coming from tempplate first_app folder"}
    return render(request,"first_app/index.html",context=date_dict)

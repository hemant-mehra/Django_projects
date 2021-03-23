from django.contrib import admin
from poll.models import Candidate,Voter

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Voter)


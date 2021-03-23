from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms
# Create your views here.
class SignUp(CreateView):
    form_class=forms.UserCreateForm
    success_url = reverse_lazy('login')# reverse_lazy is used when u want them to click submit button to change the page
    template_name='accounts/signup.html'

from django import forms
#add for validators and add validaotr in bothcatcher@@
from django.core import validators
from AppTwo.models import User

# def check_for_z(value): #**
#     if value[0].lower()!='z':
#         raise forms.ValidationError("NAME NEEDS TO START WITH Z")

class MyNewForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = []

from django import forms
#add for validators and add validaotr in bothcatcher@@
from django.core import validators

# def check_for_z(value): #**
#     if value[0].lower()!='z':
#         raise forms.ValidationError("NAME NEEDS TO START WITH Z")

class FormName(forms.Form):
    name=forms.CharField()
    # name=forms.CharField(validators=[check_for_z]) #**
    email=forms.EmailField()
    vemail=forms.EmailField(label="Enter ur email again")
    text = forms.CharField(widget=forms.Textarea)

    # botcatcher= forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])#@@

# #one method of bot cathcer
#     def clean_botcatcher(self):
#         botcatcher=self.cleaned_data['botcatcher']
#         if len(botcatcher)> 0:
#             raise forms.ValidationError("GOTCHA BOT!")
#         return botcatcher


#clean entire forms
    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data["email"]
        vemail=all_clean_data["vemail"]

        if email!=vemail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")

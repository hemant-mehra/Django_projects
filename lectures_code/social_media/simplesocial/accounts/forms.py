# gets active user at the time
from django.contrib.auth import get_user_model
# buit in UserCreationForm
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm): #class name is diffrenr the import remebmber
    class Meta:
        fields=('username','email','password1','password2')# inbuit from above password 1 and 2 are jsut confrim type
        model=get_user_model()#gets current users model



    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # my choice of costmizations
        self.fields['username'].label='Display Name'
        self.fields['email'].label='Email Address'

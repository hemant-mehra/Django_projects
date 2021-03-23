from django.forms import ModelForm
from .models import Voter,Candidate
from django import forms

men=Candidate.objects.all()
fav_man=[]
for man in men: 
    fav_man.append((man.name,man.name))

class VoteCandidateForm(forms.Form):

    your_vote= forms.CharField(label='Select who are you voting for: ', widget=forms.RadioSelect(choices=fav_man))


class VoterForm(ModelForm):
    class Meta:
        model=Voter
        fields = '__all__'




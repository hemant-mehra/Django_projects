from django.shortcuts import render
from poll.models import Candidate,Voter
from django.views.generic import TemplateView
from .forms import VoterForm,VoteCandidateForm
from django.http import HttpResponse


# Create your views here.

class CandidateView(TemplateView):

    template_name='main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['candidates'] = Candidate.objects.all()
        return context



def vote(request):

    if request.method == 'POST':
        MyVoterForm = VoterForm(request.POST)
        MyCandidateForm=VoteCandidateForm(request.POST)
      
        if MyVoterForm.is_valid() and MyCandidateForm.is_valid():
                adhar = MyVoterForm.cleaned_data['adhar_number']
                man=MyCandidateForm.cleaned_data.get('your_vote')
                
                if Voter.objects.filter(adhar_number=adhar):
                    return HttpResponse("You have already Voted")
                else:
                    voted=Candidate.objects.get(name=man)
                    
                    MyVoterForm.save()
                    voted.poll+=1
                    voted.save()
                    candidates=Candidate.objects.all()  
                    # return HttpResponse("You have voted now")
                    return render(request,"result.html",{'candidates':candidates})


    else:
        vote_form=VoterForm()
        candidate_form=VoteCandidateForm()
        candidates=Candidate.objects.all()

    return render(request,'vote.html',{'vote_form':vote_form,"candidate_form":candidate_form,'candidates':candidates})



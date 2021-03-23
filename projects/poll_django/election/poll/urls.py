from django.urls import path,include
from .views import CandidateView
from poll import views



urlpatterns = [
    path("",CandidateView.as_view(),name='list'),
    path('form/',views.vote),
]

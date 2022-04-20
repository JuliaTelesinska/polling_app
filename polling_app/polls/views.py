from django.shortcuts import render, redirect

from .models import Candidate
# Create your views here.


def starting(request):
    return render(request, 'polls/welcome.html')

def view_candidates(request):
    return render(request, 'polls/candidates.html',
                  {"candidates" : Candidate.objects.all()},)

def add_candidate(request):
    return render(request, 'polls/')

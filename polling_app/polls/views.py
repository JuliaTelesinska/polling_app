from django.shortcuts import render, redirect
from django.forms import modelform_factory
from .models import Candidate


# Create your views here.


def starting(request):
    return render(request, 'polls/welcome.html')


def view_candidates(request):
    return render(request, 'polls/candidates.html',
                  {"candidates": Candidate.objects.all()}, )


CandidateForm = modelform_factory(Candidate, exclude=[])


def add_candidate(request):
    if request.method == "POST":
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CandidateForm()
    return render(request, 'polls/add_candidate.html', {"form": form})

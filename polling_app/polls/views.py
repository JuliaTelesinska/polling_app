from django.shortcuts import render, redirect
from django.forms import modelform_factory
from .models import Candidate,Event
from django.http import HttpResponse
import csv
import codecs

# Create your views here.


def starting(request):
    return render(request, 'polls/welcome.html')


def view_candidates(request):
    return render(request, 'polls/candidates.html',
                  {"candidates": Candidate.objects.all()},)


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


EventForm = modelform_factory(Event, exclude=[])


def view_elections(request):
    return render(request, 'polls/elections.html',
                  {"events": Event.objects.all()},)


def add_election(request):
    if request.method == "POST":
        event = EventForm(request.POST)
        if event.is_valid():
            event.save()
            return redirect("home")
    else:
        event = EventForm()
    return render(request, 'polls/add_election.html', {"event": event})


def download_csv(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="election_details.csv"'},
    )
    response.write(codecs.BOM_UTF8)
    writer = csv.writer(response, delimiter=";")
    writer.writerow(["Name of event", "Date of event"])

    for event in Event.objects.all():
        row = [event.event_name, event.date]
        for candidate in event.candidate.all():
            row.append(str(candidate.first_name) + " " + str(candidate.last_name))
        writer.writerow(row)
    return response
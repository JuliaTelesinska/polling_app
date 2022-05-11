from django.shortcuts import render, redirect
from django.forms import modelform_factory
from .models import Candidate, Event, PoliticalParty
from django.http import HttpResponse
import csv
import codecs
from django.shortcuts import render
from django.core.paginator import Paginator
from .filters import CandidateFilter

def starting(request):
    return render(request, 'polls/welcome.html')

CandidateForms = modelform_factory(Candidate, exclude=[])

def add_candidate(request):
    if request.method == "POST":
        form = CandidateForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CandidateForms()
    return render(request, 'polls/add_candidate.html', {"form": form})

def view_candidates(request):
    myFilter = CandidateFilter(request.GET, queryset=Candidate.objects.all())
    candidates = myFilter.qs
    return render(request, 'polls/candidates.html',
                  {"candidates": candidates, 'myFilter': myFilter},)

EventForm = modelform_factory(Event, exclude=[])

def view_elections(request):
    events_list = Event.objects.all()
    paginator = Paginator(events_list, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'polls/elections.html', {'page_obj': page_obj})


def add_election(request):
    if request.method == "POST":
        event = EventForm(request.POST)
        if event.is_valid():
            event.save()
            return redirect("home")
    else:
        event = EventForm()
    return render(request, 'polls/add_election.html', {"event": event})

PoliticalPartyForm = modelform_factory(PoliticalParty, exclude=[])

def view_political_parties(request):
    return render(request, 'polls/political_parties.html',
                  {"political_parties": PoliticalParty.objects.all()},)

def add_political_party(request):
    if request.method == "POST":
        form = PoliticalPartyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PoliticalPartyForm()
    return render(request, 'polls/add_political_party.html', {"form": form})

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

def pie_chart(request):
    data = []
    labels = []
    for event in Event.objects.all():
        for candidate in event.candidate.all():
            if candidate.party.party_name not in labels:
                data.append(1)
                labels.append(candidate.party.party_name)
            else:
                idx = labels.index(candidate.party.party_name)
                data[idx] += 1
    return render(request, 'polls/pie_chart.html', {
        'labels': labels,
        'data': data,
    })


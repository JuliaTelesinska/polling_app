from django.contrib import admin
from .models import Candidate, Event, PoliticalParty

# Register your models here.

admin.site.register(Candidate)
admin.site.register(Event)
admin.site.register(PoliticalParty)
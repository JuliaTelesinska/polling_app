from django.contrib import admin
from .models import Candidate, Event

# Register your models here.

admin.site.register(Candidate)
admin.site.register(Event)

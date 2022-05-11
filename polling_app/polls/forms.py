from datetime import date

from django.forms import ModelForm, DateInput, TextInput
from django import forms

from .models import Candidate

class CandidateForms(ModelForm):
    class Meta:
        model = Candidate
        fields = ('first_name', 'last_name', 'party', 'age', 'candidate_picture')
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'party': 'Political party',
            'age': 'Age',
            'candidate_picture': 'Choose a picture',
        }
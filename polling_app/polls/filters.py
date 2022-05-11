import django_filters
from .models import Candidate
from django_filters import CharFilter


class CandidateFilter(django_filters.FilterSet):
   class Meta:
        model = Candidate
        fields = ['first_name', 'last_name', 'party', 'age']

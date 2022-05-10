import django_filters
from .models import Candidate
from django_filters import CharFilter


class CandidateFilter(django_filters.FilterSet):
    title = CharFilter(field_name="first_name", lookup_expr='icontains')

    class Meta:
        model = Candidate
        fields = ['first_name']
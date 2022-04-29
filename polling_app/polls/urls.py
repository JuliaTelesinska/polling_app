from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting, name="home"),
    path('candidates', views.view_candidates, name="view_candidates"),
    path('add_candidate', views.add_candidate, name="add_candidate"),
    path('elections', views.view_elections, name="view_elections"),
    path('add_election', views.add_election, name="add_election"),
    path('download_csv', views.download_csv, name="download_csv"),
]
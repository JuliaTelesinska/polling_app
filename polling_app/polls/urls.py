from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.starting, name="home"),
    path('candidates', views.view_candidates, name="candidates"),
    path('add_candidate', views.add_candidate, name="add_candidate"),
    path('elections', views.view_elections, name="elections"),
    path('add_election', views.add_election, name="add_election"),
    path('add_political_party', views.add_political_party, name="add_political_party"),
    path('political_parties', views.view_political_parties, name="view_political_parties"),
    path('download_csv', views.download_csv, name="download_csv"),
    path('pie_chart/', views.pie_chart, name="pie_chart"),
    path('filtration', views.filtration, name="filtration"),
]
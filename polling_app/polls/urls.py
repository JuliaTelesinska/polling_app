from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting, name="home"),
    path('candidates', views.view_candidates, name="view_candidates"),
    path('add_candidate', views.add_candidate, name="add_candidate"),
]
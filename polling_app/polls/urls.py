from django.urls import path
from . import views

urlpatterns = [
    path('/', views.starting),
    path('candidates', views.view_candidates),
    path('add_candidate', views.add_candidate)
]
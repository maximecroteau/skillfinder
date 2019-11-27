from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('', views.dashboard, name='dashboard'),
    path('results.json', views.resultats_json, name='resultats_json')
]
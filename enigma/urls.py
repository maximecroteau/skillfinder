from django.urls import path

from . import views

urlpatterns = [
    path('', views.enigma1, name='enigma1'),
]
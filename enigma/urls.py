from django.urls import path

from . import views

urlpatterns = [
    path('', views.enigma1_1, name='enigma1'),
    path('enigma2_1', views.enigma2_1, name='enigma2'),
]

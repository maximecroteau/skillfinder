from django.urls import path

from . import views

urlpatterns = [
    path('', views.enigma1_1, name='enigma1_1'),
    path('enigma1_2', views.enigma1_2, name='enigma1_2'),
    path('enigma1_3', views.enigma1_3, name='enigma1_3'),
    path('enigma2_1', views.enigma2_1, name='enigma2_1'),
    path('enigma2_2', views.enigma2_2, name='enigma2_2'),
    path('enigma2_3', views.enigma2_3, name='enigma2_3'),
    path('enigma3_1', views.enigma3_1, name='enigma3_1'),
    path('enigma3_2', views.enigma3_2, name='enigma3_2'),
    path('enigma3_3', views.enigma3_3, name='enigma3_3'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('Keml9HNSxUOurua', views.enigma1_1, name='enigma1_1'),
    path('1uOgaeJZ1aCZcKK', views.enigma1_2, name='enigma1_2'),
    path('hzeyGYamdVZbFcg', views.enigma1_3, name='enigma1_3'),
    path('kapo5hwGk4WO14x', views.enigma2_1, name='enigma2_1'),
    path('GWreC08xAmpUZu2', views.enigma2_2, name='enigma2_2'),
    path('ZekdITG0Tb5MD5A', views.enigma2_3, name='enigma2_3'),
    path('iRjc3peGwV2dLF9', views.enigma3_1, name='enigma3_1'),
    path('XliQeKMa6wY1z2X', views.enigma3_2, name='enigma3_2'),
    path('kpKqpcsBx6TRZ87', views.enigma3_3, name='enigma3_3'),
    path('l7jhjxdNvLLeKHj', views.etape1, name='etape1'),
    path('nKmf8hMFJ5oqBmV', views.etape2, name='etape2'),
    path('CQbrAsmm1sRXUrg', views.end, name='end'),
    path('', views.accueil, name='accueil'),
]
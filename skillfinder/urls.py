from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('rh/', include('rh.urls')),
    path('', include('enigma.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
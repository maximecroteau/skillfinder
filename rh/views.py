from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from enigma.models import Results
from django.shortcuts import redirect

from .forms import SignUpForm


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'menu/signup.html', {
        'form': form
    })


@login_required
def dashboard(request):
    resultats = Results.objects.all()
    return render(request, 'menu/dashboard.html', {
        'resultats': resultats,
    })

@login_required()
def resultats_json(request):
    results_list = Results.objects.all()
    json = serializers.serialize('json', results_list)
    return HttpResponse(json, content_type='application/json')

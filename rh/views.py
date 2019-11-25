from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import redirect

from .forms import SignUpForm


# Create your views here.


def home(request):
    return render(request, 'enigma/enigma1.html')


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
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'enigma/signup.html', {
        'form': form
    })

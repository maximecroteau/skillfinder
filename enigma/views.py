from django.shortcuts import render
from .models import Answers

from .forms import EnigmaForm


def enigma1_1(request):
    form = EnigmaForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        response = data['response']
        time = data['time']
        if response.lower() == "3":
            responses = [response, time]
            return enigma2_1(request, responses)
        else:
            form = EnigmaForm()
    else:
        form = EnigmaForm()
    return render(request, 'enigma/enigma1_1.html', {
        'form': form,
    })


def enigma1_2(request):
    form = EnigmaForm(request.POST)
    if form.is_valid():
        print()
    else:
        form = EnigmaForm()
    return render(request, 'enigma/enigma1_2.html', {

    })


def enigma1_3(request):
    form = EnigmaForm(request.POST)
    if form.is_valid():
        print()
    else:
        form = EnigmaForm()
    return render(request, 'enigma/enigma1_3.html', {

    })


def enigma2_1(request, responses):
    # print(responses[0])
    # print(responses[1])
    # form = EnigmaForm(request.POST)
    # if form.is_valid():
    #    return render(request, 'enigma/enigma2_1.html')
    # else:
    #    form = EnigmaForm()
    # return render(request, 'enigma/enigma2_1.html', {
    #    'form': form,
    # })
    return render(request, 'enigma/enigma2_1.html')


def enigma2_2(request):
    form = EnigmaForm(request.POST)
    if form.is_valid():
        print()
    else:
        form = EnigmaForm()
    return render(request, 'enigma/enigma2_2.html', {

    })


def enigma2_3(request):
    form = EnigmaForm(request.POST)
    if form.is_valid():
        print()
    else:
        form = EnigmaForm()
    return render(request, 'enigma/enigma2_3.html', {

    })


def enigma3_1(request):
    form = EnigmaForm(request.POST)
    if form.is_valid():
        print()
    else:
        form = EnigmaForm()
    return render(request, 'enigma/enigma3_1.html', {

    })


def enigma3_2(request):
    form = EnigmaForm(request.POST)
    if form.is_valid():
        print()
    else:
        form = EnigmaForm()
    return render(request, 'enigma/enigma3_2.html', {

    })


def enigma3_3(request):
    form = EnigmaForm(request.POST)
    if form.is_valid():
        print()
    else:
        form = EnigmaForm()
    return render(request, '', {

    })

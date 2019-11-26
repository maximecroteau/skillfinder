from django.shortcuts import render, redirect

from .forms import EnigmaForm


def enigma1(request):
    form = EnigmaForm(request.POST)
    if form.is_valid():

        data = form.cleaned_data
        response = data['response']
        time = data['time']
        responses = [response, time]
        return enigma2(request, responses)
    else:
        form = EnigmaForm()
    return render(request, 'enigma/enigma1.html', {
        'form': form,
    })


def enigma2(request):
    # print(responses[0])
    # print(responses[1])
    # form = EnigmaForm(request.POST)
    # if form.is_valid():
    #    return render(request, 'enigma/enigma2.html')
    # else:
    #    form = EnigmaForm()
    # return render(request, 'enigma/enigma2.html', {
    #    'form': form,
    # })
    return render(request, 'enigma/enigma2.html')

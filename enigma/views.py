from django.shortcuts import render

from .forms import EnigmaForm


def enigma1_1(request):
    form = EnigmaForm(request.POST)
    print('test')
    if form.is_valid():

        data = form.cleaned_data
        print(data)
        response = data['response']
        time = data['time']
        responses = [response, time]
        return enigma2_1(request, responses)
    else:
        form = EnigmaForm()
    return render(request, 'enigma/enigma1_1.html', {
        'form': form,
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

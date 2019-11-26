from django.shortcuts import render, redirect, HttpResponse

from .forms import EnigmaForm


def enigma1_1(request):
    form = EnigmaForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        response = data['response']
        time = data['time']
        request.session['try_11'] = request.session.get('try_11', 0) + 1
        request.session.modified = True
        print(request.session)
        if response.lower() == "3":
            request.session['t_11'] = time
            return redirect('enigma2_1')
    form = EnigmaForm()
    return render(request, 'enigma/enigma1_1.html', {
        'form': form,
    })


def enigma1_2(request):
    form = EnigmaForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        response = data['response']
        time = data['time']
        request.session['try_12'] = request.session.get('try_12', 0) + 1
        request.session.modified = True
        print(request.session)
        if response.lower() == "22":
            request.session['t_12'] = time
            return redirect('enigma2_2')
    form = EnigmaForm()
    return render(request, 'enigma/enigma1_2.html', {
        'form': form,
    })


def enigma1_3(request):
    form = EnigmaForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        response = data['response']
        time = data['time']
        request.session['try_13'] = request.session.get('try_13', 0) + 1
        request.session.modified = True
        print(request.session)
        if response.lower() == "open":
            request.session['t_13'] = time
            return redirect('enigma2_3')
    form = EnigmaForm()
    return render(request, 'enigma/enigma1_3.html', {
        'form': form,
    })


def enigma2_1(request):
    form = EnigmaForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        response = data['response']
        time = data['time']
        request.session['try_21'] = request.session.get('try_21', 0) + 1
        request.session.modified = True
        print(request.session)
        if response.lower() == "rouge":
            request.session['t_21'] = time
            return redirect('enigma3_1')
    form = EnigmaForm()
    return render(request, 'enigma/enigma2_1.html', {
        'form': form,
    })


def enigma2_2(request):
    form = EnigmaForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        response = data['response']
        time = data['time']
        request.session['try_22'] = request.session.get('try_22', 0) + 1
        request.session.modified = True
        print(request.session)
        if response.lower() == "vermeil":
            request.session['t_22'] = time
            return redirect('enigma3_2')
    form = EnigmaForm()
    return render(request, 'enigma/enigma2_2.html', {
        'form': form,
    })


def enigma2_3(request):
    form = EnigmaForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        response = data['response']
        time = data['time']
        request.session['try_23'] = request.session.get('try_23', 0) + 1
        request.session.modified = True
        print(request.session)
        if response.lower() == "herodote":
            request.session['t_23'] = time
            return redirect('enigma3_3')
    form = EnigmaForm()
    return render(request, 'enigma/enigma2_3.html', {
        'form': form,
    })


def enigma3_1(request):
    form = EnigmaForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        response = data['response']
        time = data['time']
        request.session['try_31'] = request.session.get('try_31', 0) + 1
        request.session.modified = True
        print(request.session)
        if response.lower() == "secret":
            request.session['t_31'] = time
            return redirect('enigma1_2')
    form = EnigmaForm()
    return render(request, 'enigma/enigma3_1.html', {
        'form': form,
    })


def enigma3_2(request):
    form = EnigmaForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        response = data['response']
        time = data['time']
        request.session['try_32'] = request.session.get('try_32', 0) + 1
        request.session.modified = True
        print(request.session)
        if response.lower() == "virgule":
            request.session['t_32'] = time
            return redirect('enigma1_3')
    form = EnigmaForm()
    return render(request, 'enigma/enigma3_2.html', {
        'form': form,
    })


def enigma3_3(request):
    form = EnigmaForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        response = data['response']
        time = data['time']
        request.session['try_33'] = request.session.get('try_33', 0) + 1
        request.session.modified = True
        print(request.session)
        if response.lower() == "rdvnatio":
            request.session['t_33'] = time
            return HttpResponse("Bien joué batard !")
    form = EnigmaForm()
    return render(request, 'enigma/enigma3_3.html', {
        'form': form,
    })



from django.shortcuts import render, redirect, HttpResponse

from .forms import EnigmaForm
from .forms import ContactForm

from .models import Results
import unidecode


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
        response = unidecode.unidecode(response) #remove é
        if response.lower() == "herodote" :
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
            return redirect('etape1')
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
            return redirect('etape2')
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
            return redirect('end')
    form = EnigmaForm()
    return render(request, 'enigma/enigma3_3.html', {
        'form': form,
    })


def etape1(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        firstname = data['firstname']
        lastname = data['lastname']
        mail = data['mail']
        request.session['firstname'] = firstname
        request.session['lastname'] = lastname
        request.session['mail'] = mail
        return redirect('enigma1_2')
    return render(request, 'menu/etape1.html')


def etape2(request):

    return render(request, 'menu/etape2.html')


def accueil(request):
    return render(request, 'menu/accueil.html')

def get_score(try_nb, time, score_decay): 
    time_penalty = time if time > score_decay else 1
    score_penalty = try_nb * time_penalty
    real_score = 100 - score_penalty
    return real_score if real_score > 0 else 0

def end(request):
    # 1
    try_11 = request.session.get('try_11')
    t_11 = request.session.get('t_11')
    t_s11 = t_11
    score1_1 = get_score(try_11, t_s11, 60)

    # 2
    try_21 = request.session.get('try_21')
    t_21 = request.session.get('t_21')
    t_s21 = t_21 - t_11
    score2_1 = get_score(try_21, t_s21, 60)

    # 3
    try_31 = request.session.get('try_31')
    t_31 = request.session.get('t_31')
    t_s31 = t_31 - t_21
    score3_1 = get_score(try_31, t_s31, 60)

    # 4
    try_12 = request.session.get('try_12')
    t_12 = request.session.get('t_12')
    t_s12 = t_12 - t_31
    score1_2 = get_score(try_12, t_s12, 120)

    # 5
    try_22 = request.session.get('try_22')
    t_22 = request.session.get('t_22')
    t_s22 = t_22 - t_12
    score2_2 = get_score(try_22, t_s22, 120)

    # 6
    try_32 = request.session.get('try_32')
    t_32 = request.session.get('t_32')
    t_s32 = t_32 - t_22
    score3_2 = get_score(try_32, t_s32, 120)

    # 7
    try_13 = request.session.get('try_13')
    t_13 = request.session.get('t_13')
    t_s13 = t_13 - t_32
    score1_3 = get_score(try_13, t_s13, 200)

    # 8
    try_23 = request.session.get('try_23')
    t_23 = request.session.get('t_23')
    t_s23 = t_23 - t_13
    score2_3 = get_score(try_23, t_s23, 300)

    # 9
    try_33 = request.session.get('try_33')
    t_33 = request.session.get('t_33')
    t_s33 = t_33 - t_23
    score3_3 = get_score(try_33, t_s33, 300)

    firstname = request.session.get('firstname')
    lastname = request.session.get('lastname')
    mail = request.session.get('mail')

    total_time = t_33
    total_score = (score1_1+score2_1+score3_1+score1_2+score2_2+score3_2+score1_3+score2_3+score3_3) /9

    requete = Results(time=total_time, firstname=firstname, lastname=lastname, mail=mail,
                      t_answer1_1=t_s11, tentative1_1=try_11, score1_1=score1_1,
                      t_answer1_2=t_s12, tentative1_2=try_12, score2_1=score2_1,
                      t_answer1_3=t_s13, tentative1_3=try_13, score3_1=score3_1,
                      t_answer2_1=t_s21, tentative2_1=try_21, score1_2=score1_2,
                      t_answer2_2=t_s22, tentative2_2=try_22, score2_2=score2_2,
                      t_answer2_3=t_s23, tentative2_3=try_23, score3_2=score3_2,
                      t_answer3_1=t_s31, tentative3_1=try_31, score1_3=score1_3,
                      t_answer3_2=t_s32, tentative3_2=try_32, score2_3=score2_3,
                      t_answer3_3=t_s33, tentative3_3=try_33, score3_3=score3_3,
                      score = total_score)
    requete.save()

    return render(request, 'menu/end.html')
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Rand
from django.shortcuts import redirect
from django.db.models import Sum
import requests
import datetime
from datetime import time


def calculate_sum(queryset):
    sum = 0
    for i in queryset:
        sum += i.ora_sfarsit.hour - i.ora_inceput.hour
    return sum


def get_sali_unique():
    sali_unice = {"Acvariu"}
    toate_salile = Rand.objects.all()
    for sala in toate_salile:
        if sala.get_sala() is not "":
            sali_unice.add(sala.get_sala())
    return sorted(sali_unice)


def get_zile():
    randuri = Rand.objects.all()
    rand = {}
    rand['Luni'] = luni = randuri.filter(zi='Luni')
    rand['Marti'] = randuri.filter(zi='Marti')
    rand['Miercuri'] = randuri.filter(zi='Miercuri')
    rand['Joi'] = randuri.filter(zi='Joi')
    rand['Vineri'] = randuri.filter(zi='Vineri')
    rand['Sambata'] = randuri.filter(zi='Sambata')
    rand['Duminica'] = randuri.filter(zi='Duminica')
    return rand


def verificare_disp(_sala, zi, i):
    sali = zi.filter(sala=_sala)
    t_inceput = time(i)
    t_sfarsit = time(i + 1)
    for sala in sali:
        if (
                t_sfarsit <= sala.ora_sfarsit and t_sfarsit > sala.ora_inceput or t_inceput >= sala.ora_inceput and t_inceput < sala.ora_sfarsit):
            return 0
        else:
            continue
    return 1


def program_sali(request):
    zile = ["Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", "Duminica"]
    rand = get_zile()
    sali = get_sali_unique()
    print(sali)
    ore = [time(8), time(9), time(10), time(11), time(12), time(13), time(14), time(15), time(16), time(17), time(18),
           time(19), time(20)]
    template = loader.get_template('sali_disponibile.html')
    dict = []
    for sala in range(len(sali)):
        dict2 = []
        dict.append(dict2)
        for zi in range(0, 7):
            dict3 = []
            dict[sala].append(dict3)
            for ora in range(0, 12):
                if verificare_disp(sali[sala], rand[zile[zi]], ora + 8) == 1:
                    dict[sala][zi].append("green")
                else:
                    dict[sala][zi].append("red")

    context = {'lista': dict, 'sali': sali, 'zile': zile, 'ore': range(8, 20), 'lungime': len(sali),
               'rangesali': range(len(sali)), 'rangezile': range(7), 'rangeore': range(12)}

    return HttpResponse(template.render(context, request))




def get_materii_unique():
    materii_unice = {"Introducere in criptografie"}
    toate_materiile = Rand.objects.all()
    for materie in toate_materiile:
        materii_unice.add(materie.get_materie())
    return sorted(materii_unice)


def index(request):
    if '?' not in request.get_raw_uri():
        return redirect('/orar/?grupa=I2A4')

    grupe = []
    _grupe_queryset = Rand.objects.all().values_list('grupa').distinct()
    for gr in _grupe_queryset:
        grupe.append(gr[0])
    _grupe_set = {'I1'}
    for gr in grupe:
        for aux in gr.split(','):
            _grupe_set.add(aux)
    lista_grupe = sorted(_grupe_set)

    print(datetime.datetime.now().strftime("%A"))
    randuri = Rand.objects.all()
    titlu = ""

    if "sali_libere_acum" in request.GET:
        day = datetime.datetime.now().strftime("%A")
        if day == "Monday":
            day = "Luni"
        if day == "Tuesday":
            day = "Marti"
        if day == "Wednesday":
            day = "Miercuri"
        if day == "Thursday":
            day = "Joi"
        if day == "Friday":
            day = "Vineri"
        if day == "Saturday":
            day = "Sambata"
        if day == "Sunday":
            day = "Duminica"
        print(day)
        time_hour = datetime.datetime.now().time()
        sali_ocupate = Rand.objects.filter(ora_inceput__lt=time_hour, ora_sfarsit__gt=time_hour, zi=day).distinct(
            'sala')
        randuri = randuri.exclude(sala__in=sali_ocupate.values('sala')).exclude(sala = "").distinct('sala')
        print(sali_ocupate)
        template = loader.get_template('saliLibere.html')
        context = {'grupe': lista_grupe, 'sali': get_sali_unique(), 'cursuri': get_materii_unique(), 'randuri': randuri}
        return HttpResponse(template.render(context, request))
    request_materie = ""
    request_grupa = ""
    request_sala = ""
    request_profesor = ""
    if "sala" in request.GET:
        request_sala = request.GET['sala']
        if request_sala is not "":
            randuri = randuri.filter(sala=request_sala)
            titlu = "Sala " + request_sala

    if "materie" in request.GET:
        request_materie = request.GET['materie']
        if request_materie is not "":
            randuri = randuri.filter(curs=request_materie)
            titlu = "Materia " + request_materie

    if "profesor" in request.GET:
        request_profesor = request.GET['profesor']
        if request_profesor is not "":
            randuri = randuri.filter(profesor=request_profesor)
            titlu = "Profesor " + request_profesor

    if "grupa" in request.GET:
        request_grupa = request.GET['grupa']
        if request_grupa is not "":
            grupa_len = len(request_grupa)
            randuri = randuri.filter(grupa__iregex=(r'([a-z0-9]{0})' + request_grupa + r'([a-z0-9]{0})')).exclude(
                grupa__iregex=(r'[a-z0-9]' + request_grupa)).exclude(
                grupa__iregex=(request_grupa + r'[a-z0-9]')).distinct()
            for i in range(1, grupa_len):
                req_group = request_grupa[0:i]
                print(req_group)
                randuri = randuri | randuri.filter(
                    grupa__iregex=(r'([a-z0-9]{0})' + req_group + r'([a-z0-9]{0})')).exclude(
                    grupa__iregex=(r'[a-z0-9]' + req_group)).exclude(
                    grupa__iregex=(req_group + r'[a-z0-9]')).distinct()
            titlu = "Grupa " + request_grupa

    randuri = randuri.distinct()
    randuri = randuri.order_by('ora_inceput')

    luni = randuri.filter(zi='Luni')
    marti = randuri.filter(zi='Marti')
    miercuri = randuri.filter(zi='Miercuri')
    joi = randuri.filter(zi='Joi')
    vineri = randuri.filter(zi='Vineri')
    sambata = randuri.filter(zi='Sambata')
    duminica = randuri.filter(zi='Duminica')
    template = loader.get_template('grupa.html')
    list = []

    list.append(calculate_sum(luni))
    list.append(calculate_sum(marti))
    list.append(calculate_sum(miercuri))
    list.append(calculate_sum(joi))
    list.append(calculate_sum(vineri))
    list.append(calculate_sum(sambata))
    list.append(calculate_sum(duminica))

    # grupe = Rand.objects.all().values('grupa').exclude(grupa__contains=',').distinct()
    # print(Rand.objects.values('sala').distinct())

    context = {'grupe': lista_grupe, 'sali': get_sali_unique(), 'cursuri': get_materii_unique(), 'lista_ore': list,
               'titlu': titlu, 'luni': luni, 'marti': marti, 'miercuri': miercuri, 'joi': joi, 'vineri': vineri,
               'sambata': sambata, 'duminica': duminica,'SALAH': request_sala,"GRUPAH": request_grupa, "MATERIAH": request_materie}

    return HttpResponse(template.render(context, request))

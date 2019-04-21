from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Rand
from django.db.models import Sum
import requests
import datetime
from datetime import time

def calculate_sum(queryset):
    sum = 0
    for i in queryset:
        sum+=i.ora_sfarsit.hour - i.ora_inceput.hour
    return sum

def get_sali_unique():
    sali_unice = {"Acvariu"}
    toate_salile = Rand.objects.all()
    for sala in toate_salile:
        sali_unice.add(sala.get_sala())
    return sorted(sali_unice)


def index(request):
    requested_group = request.GET['grupa']
    requested_year = request.GET['an']

    randuri = Rand.objects.filter(grupa = requested_group).filter(an = requested_year).order_by('ora_inceput')
    luni = randuri.filter(zi = 'Luni')
    marti = randuri.filter(zi = 'Marti')
    miercuri = randuri.filter(zi = 'Miercuri')
    joi = randuri.filter(zi = 'Joi')
    vineri = randuri.filter(zi = 'Vineri')
    sambata = randuri.filter(zi = 'Sambata')
    duminica = randuri.filter(zi = 'Duminica')
    template = loader.get_template('index.html')
    list = []

    list.append(calculate_sum(luni))
    list.append(calculate_sum(marti))
    list.append(calculate_sum(miercuri))
    list.append(calculate_sum(joi))
    list.append(calculate_sum(vineri))
    list.append(calculate_sum(sambata))
    list.append(calculate_sum(duminica))

    context = {'lista_ore': list,'an': requested_year, 'grupa': requested_group , 'luni': luni, 'marti': marti, 'miercuri': miercuri, 'joi': joi, 'vineri': vineri, 'sambata': sambata, 'duminica': duminica}


    return HttpResponse(template.render(context,request))

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
    sali = zi.filter(sala = _sala)
    t_inceput = time(i)
    t_sfarsit = time(i+1)
    for sala in sali:
        if(t_sfarsit<=sala.ora_sfarsit and t_sfarsit>sala.ora_inceput or t_inceput>=sala.ora_inceput and t_inceput<sala.ora_sfarsit):
            return 0
        else:
            continue
    return 1

def program_sali(request):
    zile = ["Luni","Marti","Miercuri","Joi","Vineri","Sambata","Duminica"]
    rand = get_zile()
    sali = get_sali_unique()
    ore = [time(8),time(9),time(10),time(11),time(12),time(13),time(14),time(15),time(16),time(17),time(18),time(19),time(20)]
    template = loader.get_template('sali_disponibile.html')
    dict = []
    for sala in range(len(sali)):
        dict2 = []
        dict.append(dict2)
        for zi in range(0,7):
            dict3 = []
            dict[sala].append(dict3)
            for ora in range(0,12):
                if verificare_disp(sali[sala],rand[zile[zi]],ora+8)==1:
                    dict[sala][zi].append("green")
                else:
                    dict[sala][zi].append("red")

    context = {'lista': dict,'sali': sali, 'zile': zile, 'ore': range(8,20),'lungime': len(sali), 'rangesali':range(len(sali)),'rangezile':range(7),'rangeore':range(12)}

    return HttpResponse(template.render(context, request))



from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Materie
from .models import Rand
from django.db.models import Sum
import requests
import datetime

def calculate_sum(queryset):
    sum = 0
    print(queryset)
    for i in queryset:
        sum+=i.ora_sfarsit.hour - i.ora_inceput.hour
    return sum


def index(request):
    requested_group = request.GET['grupa']
    requested_year = request.GET['an']

    randuri = Rand.objects.filter(grupa = requested_group).filter(curs__an = requested_year).order_by('ora_inceput')

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
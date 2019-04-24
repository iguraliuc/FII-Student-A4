import simplejson as simplejson
from django.http import HttpResponse, Http404

from .models import Personalise, Board, PersonaliseOrar
from users.models import FiiUser
from .forms import BoardForm
from .models import dict_ani_studiu
from orar.models import Rand
from orar.views import *
from utils import generics
from django.shortcuts import render, redirect, get_object_or_404
from django_tables2 import RequestConfig, tables
from django.urls import reverse
from django.db import connection

import os


def show_personalise(request):
    post_url = reverse('personalise_show')
    generic_objects = Personalise.objects.all()
    # filtered_objects = generic_objects
    # filtered = None
    #
    # filtered = NewsFilter(request.GET, queryset=generic_objects)
    # filtered_objects = filtered.qs
    #
    # tdelta = sum((float(i['time']) for i in connection.queries))
    # setattr(table, 'tdelta', tdelta)
    return render(request, 'show_personalise.html',
                  {'title': 'Personalise',
                   'post_url_name': 'personalise_show',
                   'post_url': post_url,
                   'objects': generic_objects,
                   # 'filtered_objects': filtered,
                   })


def show_join_board(request):
    post_url = reverse('join_board_show')
    generic_objects = Board.objects.all()

    return render(request, 'join_board.html',
                  {'title': 'Board',
                   'post_url_name': 'join_board',
                   'post_url': post_url,
                   'boards': generic_objects,
                   # 'filtered_objects': filtered,
                   })


def add_board(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.save()
            return redirect('/personalise/boards')
    else:
        form = BoardForm()
    return render(request, 'add_board.html', {'form': form})


def add_pref_board(request, uid, bid):
    data = {
        'status': 'False'
    }
    if request.method == 'POST':
        try:
            user = get_object_or_404(FiiUser, pk=uid)
            board = get_object_or_404(Board, pk=bid)
            if user and board:
                if not user.personalise:
                    p = Personalise()
                    p.save()
                    p.init_orar(user.an_studiu, user.grupa)
                    user.personalise = p
                    user.save()
                user.personalise.add_board(board)
                data['status'] = 'True'
        except Http404:
            data['message'] = 'Invalid user or board!'
    serialized_data = simplejson.dumps(data)
    return HttpResponse(serialized_data, content_type='application/json')


def remove_pref_board(request, uid, bid):
    data = {
        'status': 'False'
    }
    if request.method == 'POST':
        try:
            user = get_object_or_404(FiiUser, pk=uid)
            board = get_object_or_404(Board, pk=bid)
            if user and board:
                if user.personalise:
                    user.personalise.remove_board(board)
                    data['status'] = 'True'
        except Http404:
            data['message'] = 'Invalid user or board!'
    serialized_data = simplejson.dumps(data)
    return HttpResponse(serialized_data, content_type='application/json')


def check_joined_board(request, uid, bid):
    data = {
        'status': 'False'
    }
    try:
        user = get_object_or_404(FiiUser, pk=uid)
        board = get_object_or_404(Board, pk=bid)
        if user and board:
            if user.personalise and user.personalise.check_has_board(board):
                data['status'] = 'True'
    except Http404:
        data['message'] = 'Invalid board or user!'

    serialized_data = simplejson.dumps(data)
    return HttpResponse(serialized_data, content_type='application/json')


def check_joined_boards(request, uid):
    data = {
        'boards': []
    }
    try:
        user = get_object_or_404(FiiUser, pk=uid)
        if user:
            if user.personalise:
                data['boards'] = [str(board.id) for board in user.personalise.boards.all()]
    except Http404:
        data['message'] = 'Invalid user!'

    serialized_data = simplejson.dumps(data)
    return HttpResponse(serialized_data, content_type='application/json')

def show_orar(request):
    if '?' not in request.get_raw_uri():
        return redirect('/personalise/orar/?grupa=I' + str(dict_ani_studiu[request.user.an_studiu]) + request.user.grupa)

    grupe = []
    _grupe_queryset = Rand.objects.all().values_list('grupa').distinct()
    for gr in _grupe_queryset:
        grupe.append(gr[0])
    _grupe_set = {'I1'}
    for gr in grupe:
        for aux in gr.split(','):
            _grupe_set.add(aux)
    lista_grupe = sorted(_grupe_set)

    randuri = Rand.objects.all()
    titlu = ""


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
            randuri = randuri.filter(profesor__contains=request_profesor)
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
    template = loader.get_template('orar.html')
    list = []

    list.append(calculate_sum(luni))
    list.append(calculate_sum(marti))
    list.append(calculate_sum(miercuri))
    list.append(calculate_sum(joi))
    list.append(calculate_sum(vineri))
    list.append(calculate_sum(sambata))
    list.append(calculate_sum(duminica))

    context = {'grupe': lista_grupe, 'sali': get_sali_unique(), 'cursuri': get_materii_unique(), 'profesori': get_profesori_unique(), 'lista_ore': list,
               'titlu': titlu, 'luni': luni, 'marti': marti, 'miercuri': miercuri, 'joi': joi, 'vineri': vineri,
               'sambata': sambata, 'duminica': duminica,'SALAH': request_sala,"GRUPAH": request_grupa, "MATERIAH": request_materie, "PROFESORH": request_profesor}

    return HttpResponse(template.render(context, request))


def add_rand(request, uid, rid):
    data = {
        'status': 'False'
    }
    if request.method == 'POST':
        try:
            user = get_object_or_404(FiiUser, pk=uid)
            rand = get_object_or_404(Rand, pk=rid)
            if user and rand:
                if not user.personalise:
                    p = Personalise()
                    p.save()
                    p.init_orar(user.an_studiu, user.grupa)
                    user.personalise = p
                    user.save()
                user.personalise.add_class(rand)
                data['status'] = 'True'
        except Http404:
            data['message'] = 'Invalid user or board!'
    serialized_data = simplejson.dumps(data)
    return HttpResponse(serialized_data, content_type='application/json')


def remove_rand(request, uid, rid):
    data = {
        'status': 'False'
    }
    if request.method == 'POST':
        try:
            user = get_object_or_404(FiiUser, pk=uid)
            rand = get_object_or_404(Rand, pk=rid)
            if user and rand:
                if user.personalise:
                    user.personalise.remove_class(rand)
                    data['status'] = 'True'
        except Http404:
            data['message'] = 'Invalid user or board!'
    serialized_data = simplejson.dumps(data)
    return HttpResponse(serialized_data, content_type='application/json')


def check_rands(request, uid):
    data = {
        'rands': []
    }
    try:
        user = get_object_or_404(FiiUser, pk=uid)
        if user:
            if user.personalise:
                data['rands'] = [str(rand.rand_id) for rand in PersonaliseOrar.objects.filter(personalise=user.personalise)]
    except Http404:
        data['message'] = 'Invalid user!'

    serialized_data = simplejson.dumps(data)
    return HttpResponse(serialized_data, content_type='application/json')


def show_orar_personalised(request):
    grupe = []
    _grupe_queryset = Rand.objects.all().values_list('grupa').distinct()
    for gr in _grupe_queryset:
        grupe.append(gr[0])
    _grupe_set = {'I1'}
    for gr in grupe:
        for aux in gr.split(','):
            _grupe_set.add(aux)
    lista_grupe = sorted(_grupe_set)
    ids = [ora.rand_id for ora in PersonaliseOrar.objects.filter(personalise = request.user.personalise)]
    randuri = Rand.objects.filter(id__in=ids)
    titlu = ""


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
            randuri = randuri.filter(profesor__contains=request_profesor)
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
    template = loader.get_template('orar.html')
    list = []

    list.append(calculate_sum(luni))
    list.append(calculate_sum(marti))
    list.append(calculate_sum(miercuri))
    list.append(calculate_sum(joi))
    list.append(calculate_sum(vineri))
    list.append(calculate_sum(sambata))
    list.append(calculate_sum(duminica))

    context = {'grupe': lista_grupe, 'sali': get_sali_unique(), 'cursuri': get_materii_unique(), 'profesori': get_profesori_unique(), 'lista_ore': list,
               'titlu': titlu, 'luni': luni, 'marti': marti, 'miercuri': miercuri, 'joi': joi, 'vineri': vineri,
               'sambata': sambata, 'duminica': duminica,'SALAH': request_sala,"GRUPAH": request_grupa, "MATERIAH": request_materie, "PROFESORH": request_profesor}

    return HttpResponse(template.render(context, request))


def reset_orar(request):
    request.user.personalise.init_orar(request.user.an_studiu, request.user.grupa)
    return redirect('../')
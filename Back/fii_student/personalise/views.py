from .models import Personalise, Board
from .forms import BoardForm
from utils import generics
from django.shortcuts import render, redirect
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
                  {'title': 'PersonaliseApp',
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

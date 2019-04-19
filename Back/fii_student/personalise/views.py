from .models import PersonaliseApp, Board
from utils import generics
from django.shortcuts import render
from django_tables2 import RequestConfig, tables
from django.urls import reverse
from django.db import connection

import os


def show_personalise_app(request):
    post_url = reverse('personalise_app_show')
    generic_objects = PersonaliseApp.objects.all()
    # filtered_objects = generic_objects
    # filtered = None
    #
    # filtered = NewsFilter(request.GET, queryset=generic_objects)
    # filtered_objects = filtered.qs
    #
    # tdelta = sum((float(i['time']) for i in connection.queries))
    # setattr(table, 'tdelta', tdelta)
    return render(request, 'show_personalise_app.html',
                  {'title': 'PersonaliseApp',
                   'post_url_name': 'personalise_app_show',
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

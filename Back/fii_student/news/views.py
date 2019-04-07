from .models import News
from .filters import NewsFilter
from .tables import NewsTable
from utils import generics
from django.shortcuts import render
from django_tables2 import RequestConfig, tables
from django.urls import reverse
from django.db import connection

import os
def show_news(request):
    post_url = reverse('news_show')
    generic_objects = News.objects.all()
    # filtered_objects = generic_objects
    # filtered = table = None
    #
    # filtered = NewsFilter(request.GET, queryset=generic_objects)
    # filtered_objects = filtered.qs
    #
    # table = NewsTable(filtered_objects)
    # RequestConfig(request, paginate={"per_page": 25}).configure(table)
    #
    # tdelta = sum((float(i['time']) for i in connection.queries))
    # setattr(table, 'tdelta', tdelta)

    return render(request, 'show_news.html',
                  {'title': 'News',
                   'post_url_name': 'news_show',
                   'post_url': post_url,
                   'objects': generic_objects,
                   # 'filter': filtered,
                   })

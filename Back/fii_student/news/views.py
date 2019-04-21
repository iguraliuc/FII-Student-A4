from .models import News
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import connection
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required


@login_required
def show_news(request):
    post_url = reverse('news_show')
    generic_objects = News.objects.all()
    # print(request)
    # print(request.read())
    # filtered_objects = generic_objects
    # filtered = None
    #
    # filtered = NewsFilter(request.GET, queryset=generic_objects)
    # filtered_objects = filtered.qs
    #
    # tdelta = sum((float(i['time']) for i in connection.queries))
    # setattr(table, 'tdelta', tdelta)
    return render(request, 'show_news.html',
                  {'title': 'News',
                   'post_url_name': 'news_show',
                   'post_url': post_url,
                   'objects': generic_objects,
                   # 'filtered_objects': filtered,
                   })

class NewsDetail(DetailView):
    model = News
    # post_url = reverse('news-detail')
    template_name = "anunturi-individual.html"
    pk_url_kwarg = 'news_id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context
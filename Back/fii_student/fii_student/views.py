from django.shortcuts import render
from django.urls import reverse


def show_landing_page(request):

    return render(request, 'prezentare.html',
                  {'title': 'MainPage',
                   'post_url_name': 'show_main_page',
                   })


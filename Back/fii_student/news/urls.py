from django.urls import path

from .views import *

urlpatterns = [
    path(r'', show_news, name='news_show'),
]
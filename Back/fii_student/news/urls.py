from django.urls import path

from .views import *

urlpatterns = [
    path(r'', show_news, name='news_show'),
    path('<news_id>/', NewsDetail.as_view(), name='news-detail'),
]
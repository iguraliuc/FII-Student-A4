from django.urls import path

from .views import *

urlpatterns = [
    path(r'', show_personalise, name='personalise_show'),
    path('boards/', show_join_board, name='join_board_show')
]
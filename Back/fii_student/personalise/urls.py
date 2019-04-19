from django.urls import path

from .views import *

urlpatterns = [
    path(r'', show_personalise_app, name='personalise_app_show'),
    path('boards/', show_join_board, name='join_board_show')
]
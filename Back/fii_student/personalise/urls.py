from django.urls import path

from .views import *

urlpatterns = [
    path(r'', show_personalise, name='personalise_show'),
    path('boards/', show_join_board, name='join_board_show'),
    path('add_board/', add_board, name='add_board'),
    path('boards/add_pref_board/<int:uid>/<int:bid>', add_pref_board, name='add_pref_board'),
    path('boards/remove_pref_board/<int:uid>/<int:bid>', remove_pref_board, name='remove_pref_board'),
]
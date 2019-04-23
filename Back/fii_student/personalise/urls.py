from django.urls import path

from .views import *

urlpatterns = [
    path(r'', show_personalise, name='personalise_show'),
    path('boards/', show_join_board, name='join_board_show'),
    path('add_board/', add_board, name='add_board'),
    path('boards/add_pref_board/<int:uid>/<int:bid>', add_pref_board, name='add_pref_board'),
    path('boards/remove_pref_board/<int:uid>/<int:bid>', remove_pref_board, name='remove_pref_board'),
    path('boards/check_joined_board/<int:uid>/<int:bid>', check_joined_board, name='check_joined_board'),
    path('boards/check_joined_boards/<int:uid>', check_joined_boards, name='check_joined_boards'),
    path('orar/', show_orar, name='show_orar'),
    path('orar/add_rand/<int:uid>/<int:rid>', add_rand, name='add_rand'),
    path('orar/remove_rand/<int:uid>/<int:rid>', remove_rand, name='remove_rand'),
    path('orar/check_rands/<int:uid>', check_rands, name='check_rands'),
    path('orar/orar_personalised/', show_orar_personalised, name='show_orar_personalised'),
    path('orar/orar_personalised/reset_orar/', reset_orar, name='reset_orar'),
]
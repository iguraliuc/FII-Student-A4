from django.urls import path

from .views import *

urlpatterns = [
    path(r'', show_resources.__str__, name='resources_show'),
]
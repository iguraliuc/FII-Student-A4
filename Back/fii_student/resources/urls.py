from django.urls import path

from .views import *

urlpatterns = [
    path(r'', show_resources, name='resources_show'),
    path('<log_id>/', ResourceDetail.as_view(), name='resource-detail'),
]
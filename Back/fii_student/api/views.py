from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from news.models import News
from api.serializers import *


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-inserted_time');
    serializer_class = NewsSerializer

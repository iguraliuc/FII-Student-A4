from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import *
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-inserted_time')
    serializer_class = NewsSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('news_id', 'title', 'body', 'author_name', 'category', 'source', )


class PersonaliseViewSet(viewsets.ModelViewSet):
    queryset = Personalise.objects.all()
    serializer_class = PersonaliseSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id', 'font_family', )


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id', 'year', 'subject', 'teacher', 'description', )


class ResourcesViewSet(viewsets.ModelViewSet):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('resources_id', 'title', 'url', 'content', )


class OrarViewSet(viewsets.ModelViewSet):
    queryset = Rand.objects.all()
    serializer_class = OrarSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('curs', 'zi', 'ora_inceput', 'ora_sfarsit', 'grupa', 'tip', 'sala', 'profesor', 'pachet', )


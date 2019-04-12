from rest_framework import serializers
from news.models import News
from personaliseApp.models import PersonaliseApp


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('news_id', 'title', 'body', 'author_name', 'category')


class PersonaliseAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonaliseApp
        fields = None  # to add fields here

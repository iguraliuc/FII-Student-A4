from rest_framework import serializers
from news.models import News
from personaliseApp.models import PersonaliseApp
from resources.models import Resources


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('news_id', 'title', 'body', 'author_name', 'category')


class PersonaliseAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonaliseApp
        fields = None  # to add fields here


class ResourcesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Resources
        fields = ('log_id', 'title', 'url', 'path')
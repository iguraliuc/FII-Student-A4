from rest_framework import serializers
from news.models import News
from personalise.models import Personalise
from resources.models import Resources


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('news_id', 'title', 'body', 'author_name', 'category')


class PersonaliseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personalise
        fields = None  # to add fields here


class ResourcesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Resources
        fields = ('log_id', 'title', 'url', 'path')
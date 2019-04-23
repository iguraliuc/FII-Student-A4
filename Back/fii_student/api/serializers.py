from rest_framework import serializers
from news.models import News
from orar.models import Rand
from personalise.models import Personalise, Board
from resources.models import Resources


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('news_id', 'title', 'body', 'author_name', 'category')


class PersonaliseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personalise
        fields = None  # to add fields here


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'year', 'subject', 'teacher', 'description')


class ResourcesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resources
        fields = ('log_id', 'title', 'url', 'content')
        
class OrarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rand
        fields = ('__all__')

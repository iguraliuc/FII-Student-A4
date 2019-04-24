from rest_framework import serializers
from news.models import News
from personalise.models import Personalise, Board
from resources.models import Resources
from personalise.models import Rand
from users.models import FiiUser

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
        fields = '__all__'


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FiiUser
        fields = '__all__'

from .models import News
import django_filters
import django.forms


class NewsFilter(django_filters.FilterSet):

    class Meta:
        model = News
        fields = []


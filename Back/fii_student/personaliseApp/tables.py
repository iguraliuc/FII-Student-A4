import django_tables2
from .models import PersonaliseApp
from django.utils.html import format_html


class PersonaliseAppTable(django_tables2.Table):
    def __init__(self, *args, **kwargs):
        super(PersonaliseAppTable, self).__init__(*args, **kwargs)

    @staticmethod
    def render_timestamp(record):
        if record.timestamp:
            return record.timestamp.strftime('%Y/%m/%d %H:%M:%S')
        return "—"

    class Meta:
        model = PersonaliseApp

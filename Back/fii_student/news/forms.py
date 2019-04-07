from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = News




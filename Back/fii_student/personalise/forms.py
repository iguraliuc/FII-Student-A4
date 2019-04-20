from django import forms
from .models import Personalise


class PersonaliseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonaliseForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Personalise




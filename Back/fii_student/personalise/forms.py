from django import forms
from .models import PersonaliseApp


class PersonaliseAppForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonaliseAppForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PersonaliseApp




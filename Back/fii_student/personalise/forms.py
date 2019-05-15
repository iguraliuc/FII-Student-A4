from django import forms
from .models import Personalise, Board

YEARS = ['I', 'II', 'III']


class PersonaliseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonaliseForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Personalise
        fields = []


class BoardForm(forms.ModelForm):
    year = forms.ChoiceField(choices=[(x, x) for x in YEARS], required=True)
    subject = forms.CharField(max_length=29, required=True)
    teacher = forms.CharField(max_length=29, required=True)
    description = forms.CharField(max_length=180, required=True)

    class Meta:
        model = Board
        fields = ('year', 'subject', 'teacher', 'description')

    def __init__(self, *args, **kwargs):
        super(BoardForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs.update({'class': 'form-control'})

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User

from .models import *


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=63, required=True, help_text="Prenume este obligatoriu")
    last_name = forms.CharField(max_length=63, required=True, help_text="Numele este obligatoriu")
    email = forms.EmailField(max_length=254, help_text='Este necesara o adresa de email UAIC valida.')
    rol = forms.ChoiceField(choices=[(x, x) for x in ROLURI], required=True, help_text="")
    an_studiu = forms.ChoiceField(choices=[(x, x) for x in ANI_STUDIU])
    grupa = forms.ChoiceField(choices=[(x, x) for x in GRUPE])

    class Meta:
        model = FiiUser
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'email', 'rol', 'an_studiu', 'grupa')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs.update({'class': 'form-control'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and FiiUser.objects.filter(email=email).exists():
            raise forms.ValidationError(u'Exista deja un user cu aceasta adresa de email.')
        elif 'info.uaic.ro' not in email:
            raise forms.ValidationError(u'Adresa de email introdusa nu apartine domeniului facultatii.')
        return email

#
# class LoginForm(AuthenticationForm):
#
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#
#     def __init__(self, *args, **kwargs):
#         super(LoginForm, self).__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs.update({'class': 'form-control'})
#         self.fields['password'].widget.attrs.update({'class': 'form-control'})

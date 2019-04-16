from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager

GRUPE = ['-', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
         'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7',
         'X1', 'X2', 'X3', 'alta grupa']
ANI_STUDIU = ['-', 'I', 'II', 'III']
ROLURI = ['-', 'Profesor', 'Student', 'Masterand', 'Doctorand']


class FiiUser(AbstractBaseUser):
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    first_name = models.CharField(_('first name'), max_length=63, blank=True)
    last_name = models.CharField(_('last name'), max_length=63, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    rol = models.CharField(max_length=20, choices=[(x, x) for x in ROLURI])
    an_studiu = models.CharField(max_length=20, choices=[(x, x) for x in ANI_STUDIU])
    grupa = models.CharField(max_length=20, choices=[(x, x) for x in GRUPE])
    objects = UserManager()
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email', 'first_name', 'user_name', 'rol']
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

from django.db import models

# Create your models here.


class Rand(models.Model):
    curs = models.CharField(max_length=100)
    zi = models.CharField(max_length=15)
    ora_inceput = models.TimeField(auto_now_add=True)
    ora_sfarsit = models.TimeField(auto_now_add=True)
    an = models.IntegerField(default=None, blank=True, null=True)
    grupa = models.CharField(max_length=5)
    tip = models.CharField(max_length=20)
    sala = models.CharField(max_length=20)
    profesor = models.CharField(max_length=60)
    pachet = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return self.zi
    def get_sala(self):
        return self.sala
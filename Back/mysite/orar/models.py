from django.db import models

# Create your models here.

class Sala(models.Model):
    nume_sala = models.CharField(max_length=15)
    etaj = models.IntegerField()
    echipari = models.CharField(max_length=50)

    def __str__(self):
        return self.nume_sala


class Materie(models.Model):
    titlu_curs = models.CharField(max_length=51)
    credite = models.IntegerField()
    an = models.IntegerField()
    semestru = models.IntegerField()

    def __str__(self):
        return self.titlu_curs

class Profesor(models.Model):
    nume = models.CharField(max_length=31)
    prenume = models.CharField(max_length=51)
    materii = models.ManyToManyField(Materie)
    grad_didactic = models.CharField(max_length=31)
    cabinet = models.ForeignKey(Sala, on_delete=models.CASCADE)

    def __str__(self):
        return self.nume + self.prenume

class Rand(models.Model):
    curs = models.ForeignKey(Materie,default=0, on_delete=models.CASCADE)
    zi = models.CharField(max_length=15)
    ora = models.TimeField()
    grupa = models.CharField(max_length=5)
    tip = models.CharField(max_length=20)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return self.zi
# from django.contrib.postgres.fields import ArrayField
from django.db import models


#  -- DUMMY MODELS --


class Student(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    year = models.IntegerField(default=1)
    semian = models.CharField(max_length=5)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)


class Board(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')

# -------------------


class PersonaliseApp(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='ID')  # dunno if needed yet
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)

    class Meta:
        db_table = 'personaliseApp'

    def __str__(self):
        return '{}'.format(self.title)

# from django.contrib.postgres.fields import ArrayField
from django.db import models

# from users.models import FiiUser
from orar.models import Rand

#  -- DUMMY MODELS --


class Student(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    year = models.IntegerField(default=1)
    semian = models.CharField(max_length=5)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.id)

# -------------------


class Board(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    year = models.IntegerField(default=1)
    subject = models.CharField(max_length=255, null=True)
    teacher = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return '{}'.format(self.id)


class PersonaliseApp(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='ID')  # dunno if needed yet
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # _id
    boards = models.ManyToManyField(Board)  # ), on_delete=models.CASCADE)  # _id
    classes = models.ManyToManyField(Rand)

    class Meta:
        db_table = 'personaliseApp'
        managed = True

    def __str__(self):
        return 'Student[{}] -> Boards[{}]'.format(self.student.id, 0)  # [board.id for board in self.boards.all()])

    def init_orar(self):
        # search classes
        # self.boards.add()
        pass
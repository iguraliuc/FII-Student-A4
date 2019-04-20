# from django.contrib.postgres.fields import ArrayField
from django.db import models

# from users.models import FiiUser
from orar.models import Rand, Materie

#  -- DUMMY MODELS --

GRUPE = ['-', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
         'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7',
         'X1', 'X2', 'X3', 'alta grupa']
ANI_STUDIU = ['-', 'I', 'II', 'III']
dict_ani_studiu = {
    '-': 0,
    'I': 1,
    'II': 2,
    'III': 3
}

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


class Personalise(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='ID')  # dunno if needed yet
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # _id
    boards = models.ManyToManyField(Board)  # ), on_delete=models.CASCADE)  # _id
    classes = models.ManyToManyField(Rand)

    class Meta:
        db_table = 'personalise'
        managed = True

    def __str__(self):
        return 'Student[{}] -> Boards[{}]'.format(self.student.id, 0)  # [board.id for board in self.boards.all()])

    def init_orar(self):
        v_materii = Materie.objects.filter(an=self.student.year)
        for v_materie in v_materii:
            v_id = v_materie.id
            for v_rand in Rand.objects.filter(curs=v_id):
                self.classes.add(v_rand)

    def add_class(self, rand):
        if not isinstance(rand, Rand):
            return False
        self.classes.add(rand)

    def remove_class(self, rand):
        if not isinstance(rand, Rand):
            return False
        self.classes.remove(rand)

    def add_board(self, board):
        if not isinstance(board, Board):
            return False
        self.boards.add(board)

    def remove_board(self, board):
        if not isinstance(board, Board):
            return False
        self.boards.add(board)
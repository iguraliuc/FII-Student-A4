# from django.contrib.postgres.fields import ArrayField
from django.db import models

# from users.models import FiiUser
from orar.models import Rand

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
    year = models.CharField(max_length=20, choices=[(x, x) for x in ANI_STUDIU])
    subject = models.CharField(max_length=255, null=True, unique=True)
    teacher = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return '{}'.format(self.id)


class Personalise(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='ID')  # dunno if needed yet
    # user = models.ForeignKey(Student, on_delete=models.CASCADE)  # _id
    boards = models.ManyToManyField(Board)  #, through='PersonaliseBoard')  # ), on_delete=models.CASCADE)  # _id
    classes = models.ManyToManyField(Rand, through='PersonaliseOrar')

    class Meta:
        db_table = 'personalise'
        managed = True

    def __str__(self):
        return 'Boards[{}]'.format(0)  # [board.id for board in self.boards.all()])

    def init_orar(self, an, grupa):
        if an and an != '-' and grupa and grupa != '-' and an in dict_ani_studiu.keys():
            for v_rand in Rand.objects.filter(an=dict_ani_studiu[an], grupa=grupa):
                PersonaliseOrar.objects.create(personalise=self, rand=v_rand)
                # self.classes.add(v_rand)
            return True
        return False

    def add_class(self, rand):
        if not isinstance(rand, Rand):
            return False
        # self.classes.add(rand)
        PersonaliseOrar.objects.create(personalise=self, rand=rand)

    def remove_class(self, rand):
        if not isinstance(rand, Rand):
            return False
        # self.classes.remove(rand)
        self.classes.delete(rand=rand)

    def add_board(self, board):
        if not isinstance(board, Board):
            return False
        self.boards.add(board)

    def remove_board(self, board):
        if not isinstance(board, Board):
            return False
        self.boards.remove(board)

    def check_has_board(self, board):
        if not isinstance(board, Board) or len(self.boards.filter(pk=board.id)) == 0:
            return False
        return True


# intermediate model for extra data in ManyToManyField for personalise -> classes
class PersonaliseOrar(models.Model):
    personalise = models.ForeignKey(Personalise, on_delete=models.CASCADE)
    rand = models.ForeignKey(Rand, on_delete=models.CASCADE)
    alert = models.BooleanField(default=False, verbose_name='ALERT')


class PersonaliseBoard(models.Model):
    # extra data for each board chosen
    pass

# from django.contrib.postgres.fields import ArrayField
from django.db import models

# from users.models import FiiUser
from orar.models import Rand

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

FONT_FAMILY_CHOICES = [
    "Roboto",
    "Arvo",
    "Montsserat",
    "Lato",
    "Inconsolata",
    "Roboto Condensed"
]
DEFAULT_COLOURS = {
    "background": "#ffffff",
    "navbar": "#000000",
    "accent": "#ff0000",
    "font": "#000000"
}
DEFAULT_FONT_FAMILY = "Arvo"


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
    boards = models.ManyToManyField(Board)  # through='PersonaliseBoard'
    classes = models.ManyToManyField(Rand, through='PersonaliseOrar')


    navbar_color = models.CharField(max_length=255, null=False, default=DEFAULT_COLOURS["navbar"])
    background_color = models.CharField(max_length=255, null=False, default=DEFAULT_COLOURS["background"])
    accent_color = models.CharField(max_length=255, null=False, default=DEFAULT_COLOURS["accent"])
    font_color = models.CharField(max_length=255, null=False, default=DEFAULT_COLOURS["font"])
    font_family = models.CharField(max_length=255, choices=[(x, x) for x in FONT_FAMILY_CHOICES], default=DEFAULT_FONT_FAMILY)

    class Meta:
        db_table = 'personalise'
        managed = True

    def __str__(self):
        return 'Boards[{}]'.format(0)  # [board.id for board in self.boards.all()])

    def init_orar(self, an, grupa):
        PersonaliseOrar.objects.filter(personalise=self).delete()
        if an and an != '-' and grupa and grupa != '-' and an in dict_ani_studiu.keys():
            for v_rand in Rand.objects.filter(grupa = "I" + str(dict_ani_studiu[an]) + grupa):
                PersonaliseOrar.objects.create(personalise=self, rand=v_rand)
            return True
        return False

    def add_class(self, rand):
        if not isinstance(rand, Rand):
            return False
        PersonaliseOrar.objects.create(personalise=self, rand=rand)
        return True

    def remove_class(self, rand):
        if not isinstance(rand, Rand):
            return False
        PersonaliseOrar.objects.filter(personalise=self, rand=rand).delete()
        return True

    def add_board(self, board):
        if not isinstance(board, Board):
            return False
        self.boards.add(board)
        return True

    def remove_board(self, board):
        if not isinstance(board, Board):
            return False
        self.boards.remove(board)
        return True

    def check_has_board(self, board):
        if not isinstance(board, Board) or len(self.boards.filter(pk=board.id)) == 0:
            return False
        return True


# intermediate model for extra data in ManyToManyField for personalise -> classes
class PersonaliseOrar(models.Model):
    personalise = models.ForeignKey(Personalise, on_delete=models.CASCADE)
    rand = models.ForeignKey(Rand, on_delete=models.CASCADE)
    alert = models.BooleanField(default=False, verbose_name='ALERT')


class Card(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    personalise = models.ForeignKey(Personalise, on_delete=models.CASCADE)
    # orderNumber = models.IntegerField(default=0, null=False)
    type = models.CharField(default=None, verbose_name='TYPE', max_length=50)
    f_key = models.IntegerField(default=None, null=True)
    x = models.IntegerField(default=1)
    y = models.IntegerField(default=1)
    width = models.IntegerField(default=1)  # max = 12
    height = models.IntegerField(default=1)

    # TODO: add function to get object in accordance with choice field

    def __str__(self):
        return '{}'.format(self.id)

    def is_valid(self):
        return True

    def getJSON(self):
        data = dict(
            id=self.id,
            type=self.type,
            x=self.x,
            y=self.y,
            width=self.width,
            height=self.height,
            data={}
        )
        return data


class PersonaliseBoard(models.Model):
    # extra data for each board chosen
    pass

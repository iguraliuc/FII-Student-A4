from django.db import models


class Student(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')


class PersonaliseApp(models.Model):

    # TODO: create db model
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    year = models.IntegerField(default=1)
    semian = models.CharField(max_length=5)

    class Meta:
        db_table = 'personaliseApp'

    def __str__(self):
        return '{}'.format(self.title)

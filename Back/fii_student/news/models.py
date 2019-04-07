from django.db import models


class News(models.Model):

    log_id = models.AutoField(primary_key=True, verbose_name='ID')
    title = models.CharField(max_length=128)
    timestamp = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    body = models.TextField()

    class Meta:
        db_table = 'announces'

    def __str__(self):
        return '{}'.format(self.title)

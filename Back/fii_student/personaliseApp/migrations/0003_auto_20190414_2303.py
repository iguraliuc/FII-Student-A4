# Generated by Django 2.1.7 on 2019-04-14 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personaliseApp', '0002_auto_20190414_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='subject',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='board',
            name='year',
            field=models.IntegerField(default=1),
        ),
    ]
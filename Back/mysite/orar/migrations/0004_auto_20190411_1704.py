# Generated by Django 2.1.7 on 2019-04-11 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orar', '0003_auto_20190411_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesor',
            old_name='grad_didacitc',
            new_name='grad_didactic',
        ),
    ]

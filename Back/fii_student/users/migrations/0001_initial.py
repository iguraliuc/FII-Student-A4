# Generated by Django 2.1.2 on 2019-04-16 12:49

from django.db import migrations, models
import users.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FiiUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=63, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=63, verbose_name='last name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('rol', models.CharField(choices=[('Profe', 'Profesor'), ('Stude', 'Student'), ('Maste', 'Masterand'), ('Docto', 'Doctorand')], max_length=20)),
                ('tip_studii', models.CharField(choices=[('Licenta', 'Licenta'), ('Master', 'Master'), ('Doctorat', 'Doctorat')], max_length=20)),
                ('an_studiu', models.CharField(choices=[('I', 'I'), ('II', 'II'), ('III', 'III')], max_length=20)),
                ('grupa', models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('A5', 'A5'), ('A6', 'A6'), ('A7', 'A7'), ('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('B4', 'B4'), ('B5', 'B5'), ('B6', 'B6'), ('B7', 'B7'), ('X1', 'X1'), ('X2', 'X2'), ('X3', 'X3'), ('alta grupa', 'alta grupa')], max_length=20)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
    ]
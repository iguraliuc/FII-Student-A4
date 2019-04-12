# Generated by Django 2.1.7 on 2019-04-09 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlu_curs', models.CharField(max_length=51)),
                ('credite', models.IntegerField()),
                ('an', models.IntegerField()),
                ('semestru', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=31)),
                ('prenume', models.CharField(max_length=51)),
                ('grad_didacitc', models.CharField(max_length=31)),
                ('cabinet', models.CharField(max_length=15)),
                ('materii', models.ManyToManyField(to='orar.Materie')),
            ],
        ),
        migrations.CreateModel(
            name='Rand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlu_curs', models.CharField(max_length=51)),
                ('zi', models.CharField(max_length=15)),
                ('ora', models.TimeField()),
                ('grupa', models.CharField(max_length=5)),
                ('tip', models.CharField(max_length=20)),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orar.Profesor')),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume_sala', models.CharField(max_length=15)),
                ('etaj', models.IntegerField()),
                ('echipari', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='rand',
            name='sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orar.Sala'),
        ),
    ]

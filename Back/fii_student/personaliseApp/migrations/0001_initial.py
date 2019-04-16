# Generated by Django 2.1.7 on 2019-04-14 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PersonaliseApp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('board_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personaliseApp.Board')),
            ],
            options={
                'db_table': 'personaliseApp',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=1)),
                ('semian', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='personaliseapp',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personaliseApp.Student'),
        ),
    ]
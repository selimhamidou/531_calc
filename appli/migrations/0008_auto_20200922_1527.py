# Generated by Django 3.1 on 2020-09-22 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0007_daily_record_max_of_the_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Exercice',
        ),
        migrations.DeleteModel(
            name='Exercise_weight',
        ),
        migrations.RenameField(
            model_name='daily_record',
            old_name='utilisateur',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='weekly_routine',
            old_name='nombre_reps_serie1',
            new_name='number_reps_set1',
        ),
        migrations.RenameField(
            model_name='weekly_routine',
            old_name='nombre_reps_serie2',
            new_name='number_reps_set2',
        ),
        migrations.RenameField(
            model_name='weekly_routine',
            old_name='nombre_reps_serie3',
            new_name='number_reps_set3',
        ),
        migrations.RenameField(
            model_name='weekly_routine',
            old_name='nombre_series',
            new_name='number_sets',
        ),
        migrations.RenameField(
            model_name='weekly_routine',
            old_name='temps_recup',
            new_name='rest_time',
        ),
        migrations.RemoveField(
            model_name='weekly_routine',
            name='nombre_reps_serie4',
        ),
        migrations.RemoveField(
            model_name='weekly_routine',
            name='nombre_reps_serie5',
        ),
        migrations.RenameModel(
            old_name='Utilisateur',
            new_name='User',
        ),
        migrations.DeleteModel(
            name='Programme',
        ),
        migrations.AddField(
            model_name='program',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli.user'),
        ),
    ]

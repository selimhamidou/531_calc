# Generated by Django 3.1.1 on 2020-09-27 10:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0013_auto_20200925_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_record',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 27, 10, 25, 44, 963031)),
        ),
    ]
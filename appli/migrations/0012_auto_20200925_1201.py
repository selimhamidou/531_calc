# Generated by Django 3.1.1 on 2020-09-25 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0011_auto_20200922_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_record',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 25, 12, 1, 4, 195533)),
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-30 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0015_auto_20200930_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_record',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 30, 9, 52, 41, 139237)),
        ),
    ]

# Generated by Django 3.1 on 2020-08-28 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0005_auto_20200828_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_record',
            name='date',
            field=models.DateField(),
        ),
    ]
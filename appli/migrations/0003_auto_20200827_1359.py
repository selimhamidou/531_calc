# Generated by Django 3.1 on 2020-08-27 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0002_daily_record'),
    ]

    operations = [
        migrations.RenameField(
            model_name='daily_record',
            old_name='max_weight',
            new_name='weight',
        ),
    ]
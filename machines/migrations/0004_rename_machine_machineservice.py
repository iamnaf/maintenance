# Generated by Django 3.2.6 on 2021-09-16 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0003_auto_20210915_2211'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Machine',
            new_name='MachineService',
        ),
    ]
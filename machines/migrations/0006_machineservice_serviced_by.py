# Generated by Django 3.2.6 on 2021-09-16 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0005_machinereport_report_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='machineservice',
            name='serviced_by',
            field=models.CharField(default='Maintenance Department', max_length=200),
            preserve_default=False,
        ),
    ]

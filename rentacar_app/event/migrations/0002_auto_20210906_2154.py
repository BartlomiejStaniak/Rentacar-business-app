# Generated by Django 3.2.3 on 2021-09-06 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='day_ended',
            field=models.DateTimeField(choices=[('1', '1'), ('2', '2'), ('3', '3')]),
        ),
        migrations.AlterField(
            model_name='event',
            name='day_started',
            field=models.DateTimeField(choices=[('1', '1'), ('2', '2'), ('3', '3')]),
        ),
    ]

# Generated by Django 3.0.6 on 2020-06-03 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeslots', '0002_timeslot_session_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='pending_until',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='session_key',
            field=models.CharField(default=None, max_length=32, null=True),
        ),
    ]

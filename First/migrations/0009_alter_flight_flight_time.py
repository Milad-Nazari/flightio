# Generated by Django 3.2.8 on 2021-11-09 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First', '0008_alter_flight_flight_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='Flight_Time',
            field=models.DateTimeField(),
        ),
    ]

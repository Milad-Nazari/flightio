# Generated by Django 3.2.8 on 2021-11-09 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First', '0013_auto_20211109_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='Flight_Date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Flight_Time',
            field=models.DateTimeField(),
        ),
    ]

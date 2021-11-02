# Generated by Django 3.2.8 on 2021-11-02 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First', '0005_alter_flight_flight_nomber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='Flight_Airline',
            field=models.CharField(choices=[('IR', 'iranair'), ('W5', 'mahan'), ('B9', 'airtour'), ('EP', 'aseman'), ('ZV', 'zagros'), ('KIH', 'kish'), ('QB', 'qeshm'), ('I3', 'ata'), ('JI', 'meraj'), ('HH', 'taban'), ('Rv', 'caspian'), ('Nv', 'karon'), ('ISS', 'sepehran'), ('VR', 'varesh'), ('PR', 'flypersia')], max_length=10),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Flight_Distination',
            field=models.CharField(choices=[('تهران', 'tehran'), ('ABD', 'abadan'), ('MHD', "mash'had"), ('SYZ', 'shiraz'), ('IFN', 'isfahan'), ('ZBR', 'chabahar')], max_length=30),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Flight_Nomber',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Flight_Origin',
            field=models.CharField(choices=[('تهران', 'tehran'), ('ABD', 'abadan'), ('MHD', "mash'had"), ('SYZ', 'shiraz'), ('IFN', 'isfahan'), ('ZBR', 'chabahar')], max_length=30),
        ),
    ]

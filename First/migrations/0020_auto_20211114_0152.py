# Generated by Django 3.2.8 on 2021-11-13 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('First', '0019_auto_20211113_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Flight_Distination',
            field=models.CharField(choices=[('tehran', 'tehran'), ('abadan', 'abadan'), ('mashhad', "mash'had"), ('shiraz', 'shiraz'), ('isfahan', 'isfahan'), ('chabahar', 'chabahar')], max_length=30),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Flight_Origin',
            field=models.CharField(choices=[('tehran', 'tehran'), ('abadan', 'abadan'), ('mashhad', "mash'had"), ('shiraz', 'shiraz'), ('isfahan', 'isfahan'), ('chabahar', 'chabahar')], max_length=30),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='title',
            field=models.CharField(choices=[('sepehr238', 'sepehr238'), ('sepehr239', 'sepehr239'), ('sepehr240', 'sepehr240'), ('sepehr250', 'sepehr250'), ('sepehr251', 'sepehr251'), ('sepehr252', 'sepehr252'), ('sepehr253', 'sepehr253')], max_length=50),
        ),
        migrations.CreateModel(
            name='SupplierComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_reply', models.BooleanField(default=False)),
                ('body', models.TextField(max_length=700)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rscomment', to='First.suppliercomment')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pscomment', to='First.supplier')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uscomment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schadulestatus', models.CharField(choices=[('start', 'start'), ('shouting', 'shouting'), ('done', 'done')], max_length=30)),
                ('flight', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='First.flight')),
            ],
        ),
    ]

from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.db.models.fields import BooleanField
from django.db.models.fields import related
from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.forms import widgets
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Flight(models.Model):
    iranair = 'iranair'
    mahan = 'mahan'
    airtour = 'airtour'
    aseman = 'aseman'
    zagros = 'zagros'
    kish = 'kish'
    qeshm = 'qeshm'
    ata = 'ata'
    meraj = 'meraj'
    taban = 'taban'
    caspian='caspian'
    karoon = 'karoon'
    sepehran_ = "sepehran_"
    varesh='varesh'
    flypersia = 'flypersia'
    
    tehran='tehran'
    abadan='abadan'
    isfahan='isfahan'
    ahvaz='ahvaz'
    tabriz= 'tabriz'
    kish='kish'
    chabahar='chabahar'
    khoramabad='khoramabad'
    shiraz='shiraz'
    kermanshah='kermanshah'
    mashhad='mashhad'

    started= 'start'
    shouting='shouting'
    done='done'
    
    City=[
        (tehran,'tehran'),
        (abadan,'abadan'),
        (mashhad,"mash'had"),
        (shiraz,'shiraz'),
        (isfahan,'isfahan'),
        (chabahar,'chabahar'),
    ]
    
    Airline =[
        (iranair,'iranair'),(mahan,'mahan'),(airtour,'airtour'),(aseman,'aseman'),(zagros,'zagros'),(kish,'kish'),
        (qeshm,'qeshm'),(ata,'ata'),(meraj,'meraj'),(taban,'taban'),(caspian,'caspian'),(karoon,'karon'),(sepehran_,'sepehran'),
        (varesh,'varesh'),(flypersia,'flypersia'),

    ]
    Flight_Origin = models.CharField(max_length=30,choices=City,)
    Flight_Distination = models.CharField(max_length=30,choices=City)
    Flight_Airline = models.CharField(max_length=10,choices=Airline)
    Flight_Nomber = models.CharField(max_length=10)
    Flight_Date = models.DateField()
    Flight_Time = models.TimeField()
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True,null=True)
    # is_valid = BooleanField(default=False)
    schadule_Date = models.DateField()
    schadule_Time = models.TimeField()


    def __str__(self):
        return f'{self.Flight_Nomber} {self.Flight_Origin} to {self.Flight_Distination} in {self.Flight_Date} at {self.Flight_Time} '

class status(models.Model):
    start='start'
    shouting='shouting'
    done='done'
    status=[(start,'start'),(shouting,'shouting'),(done,'done')]
    flight = models.OneToOneField(Flight,on_delete=models.CASCADE)
    schadulestatus = models.CharField(max_length=30,choices=status)
  
def save_profile(sender, **kwargs):
    if kwargs['created']:
        p1 = status(flight=kwargs['instance'])
        p1.schadulestatus = 'start'
        p1.save()

#call a function when schadule registerd!
post_save.connect(save_profile,sender=Flight)



class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='ucomment')
    Flight = models.ForeignKey(Flight, on_delete=models.CASCADE,related_name='pcomment')
    reply = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='rcomment')
    is_reply = models.BooleanField(default=False)
    body = models.TextField(max_length=700)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'{self.user} - {self.body[:30]}'

    class Meta:
        ordering = ('-created',)

class supplier(models.Model):
    sepehr238='sepehr238'
    sepehr239='sepehr239'
    sepehr240='sepehr240'
    sepehr250='sepehr250'
    sepehr251='sepehr251'
    sepehr252='sepehr252'
    sepehr253='sepehr253'
    suppliers=[(sepehr238,'sepehr238'),(sepehr239,'sepehr239'),(sepehr240,'sepehr240'),(sepehr250,'sepehr250'),(sepehr251,'sepehr251'),(sepehr252,'sepehr252'),(sepehr253,'sepehr253')]
    title = models.CharField(max_length=50,choices=suppliers)
    Flight = models.ForeignKey(Flight, on_delete=models.CASCADE,related_name='fsupplier')
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True,null=True)
    

class SupplierComment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='uscomment')
    supplier = models.ForeignKey(supplier, on_delete=models.CASCADE,related_name='pscomment')
    reply = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='rscomment')
    is_reply = models.BooleanField(default=False)
    body = models.TextField(max_length=700)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'{self.user} - {self.body[:30]}'

    class Meta:
        ordering = ('-created',) 
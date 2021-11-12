from django import forms
from django.db.models.fields import AutoField
from django.forms import fields
from .models import Flight,Comment
from bootstrap_datepicker_plus import DatePickerInput
from django.forms import  DateTimeField, DateInput
from bootstrap_datepicker_plus.widgets import DatePickerInput

class AddSchaduleForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields =('Flight_Origin','Flight_Distination','Flight_Airline','Flight_Nomber','Flight_Date','Flight_Time','schadule_Date','schadule_Time')


class AddCommentFlight(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('body',)
        exclude = ['createed',]
        widgets ={
            'body': forms.Textarea(attrs={'class':'form-control'})
        }
        error_messages = {
            'body':{
            'required':'این فیلد اجباری می‌باشد',
        }}
        help_text={
            'body':'max 700 cracters'
        }



class AddReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        exclude = ['created',]
        get_latest_by = ("ucomment",)
        
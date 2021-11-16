from django import forms
from django.db.models.fields import AutoField
from django.forms import fields, widgets
from .models import Flight,Comment,SupplierComment
from bootstrap_datepicker_plus import DatePickerInput
from django.forms import  DateTimeField, DateInput
from bootstrap_datepicker_plus.widgets import DatePickerInput
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime




class AddSchaduleForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields =('Flight_Origin','Flight_Distination','Flight_Airline','Flight_Nomber','Flight_Date','Flight_Time','schadule_Date','schadule_Time')
        
        widgets ={
            'flight_Origin': forms.CheckboxInput(attrs={'class':'custom-select custom-select-lg mb-3'})
        }   
    def __init__(self, *args, **kwargs):
        super(AddSchaduleForm, self).__init__(*args, **kwargs)
        self.fields['Flight_Date'] = SplitJalaliDateTimeField(label=('Flight_Date'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )

        # you can added a "class" to this field for use your datepicker!
        # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})

        self.fields['schadule_Date'] =  SplitJalaliDateTimeField(label=('schadule_Date'), 
            widget=AdminJalaliDateWidget # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
        )
        self.fields['schadule_Time'] =  SplitJalaliDateTimeField(label=('schadule_Time'), 
            widget=AdminJalaliDateWidget # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
        )
        self.fields['schadule_Date'] =  SplitJalaliDateTimeField(label=('schadule_Date'), 
            widget=AdminJalaliDateWidget # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
        )
        
        

class AddCommentFlight(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
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
class AddCommentSupplier(forms.ModelForm):
    class Meta:
        model = SupplierComment
        fields = ('body',)
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

class AddReplySupplierForm(forms.ModelForm):
    class Meta:
        model = SupplierComment
        fields = ('body',)

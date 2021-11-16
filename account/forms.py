from django import forms
from django.contrib import messages
from django.forms import fields
from django.forms.forms import Form   


messages = {
    'required':'این فیلد اجباری می‌باشد',
    'invalid':'لطفا یک ایمیل معتبر وارد نمایید',
    'max_length':'تغداد کاراکترها بیشتر از حد مجاز می‌باشد',
}


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30,help_text='max 500 caracters', widget=forms.TextInput(attrs={'class':'mb-3 form-control',"type":"username","name":"username" ,"placeholder":"username" }))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class':'mb-3 form-control',"type":"password","name":"password" , 'placeholder':'password'}))

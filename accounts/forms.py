from django.contrib.auth.models import User
from accounts.models import vendor,customer
from django import forms


class Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=vendor
        fields=['name','shopname','shopaddress','shopLicienceName_img','latitude','longitude','email','phone','password1','password2']

class customerprofile(forms.ModelForm):
    class Meta:
        model=customer
        fields=['username','firstname','lastname','email','address','street','city','email','state','pincode','phoneNo','password1','password2']

    

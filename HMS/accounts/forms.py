from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField



class Usercreationform(UserCreationForm):
    email=forms.EmailField(required=True)
    phone_number=PhoneNumberField(required=True)
     
    class Meta:
        model=User
        fields=['username','email','phone_number','password','password2']
    
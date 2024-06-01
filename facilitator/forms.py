'''
Handles creation of forms
'''

from django import forms
from django.contrib.auth.models import User
from . import models

class FacilitatorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class FacilitatorForm(forms.ModelForm):
    class Meta:
        model=models.Facilitator
        fields=['address','email','mobile','profile_pic']

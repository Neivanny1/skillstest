from django import forms
from django.contrib.auth.models import User
from .import models

'''
Generating signup form
'''
class ParticipantUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        
class ParticipantForm(forms.ModelForm):
    class Meta:
        model = models.Participant
        fields = ['address','mobile','profile_pic']
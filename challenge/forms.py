from django import forms
from django.contrib.auth.models import User
from . import models
'''
A from for capturing data from contact us page
'''
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class FacilitatorPayForm(forms.Form):
    salary  =forms.IntegerField()

class SpecialityForm(forms.ModelForm):
    class Meta:
        model = models.Speciality
        fields = ['speciality_name','question_number','total_marks','time_limit','free_or_paid', 'amount']

class QuestionForm(forms.ModelForm):
    '''
    this will show dropdown __str__ method course model is shown on html so override it
    to_field_name this will fetch corresponding value  user_id present in course model and return it
    '''
    specialityID = forms.ModelChoiceField(queryset=models.Speciality.objects.all(), empty_label="Speciality Name", to_field_name="id")
    class Meta:
        model = models.Question
        fields = ['specialityID', 'question', 'marks', 'option1', 'option2', 'option3', 'option4', 'answer']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})
        }
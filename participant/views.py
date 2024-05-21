from django.shortcuts import render
from .import forms
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from challenge import models as QMODEL
from datetime import datetime

def participanthome(request):
    current_time = datetime.now()
    context = {
        'current_time': current_time
    }
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'participant/home.html', context)

def is_participant(user):
    return user.groups.filter(name='PARTICIPANT').exists()

def participant_signup_view(request):
    userForm = forms.ParticipantUserForm()
    participantForm = forms.ParticipantForm()
    mydict={'userForm':userForm,'participantForm':participantForm}
    if request.method == 'POST':
        userForm = forms.ParticipantUserForm(request.POST)
        participantForm = forms.ParticipantForm(request.POST,request.FILES)
        if userForm.is_valid() and participantForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            participant = participantForm.save(commit=False)
            participant.user=user
            participant.save()
            my_participant_group = Group.objects.get_or_create(name='PARTICIPANT')
            my_participant_group[0].user_set.add(user)
        return HttpResponseRedirect('participantlogin')
    return render(request,'participant/signup.html',context=mydict)


@login_required(login_url='participantlogin')
@user_passes_test(is_participant)
def participant_dashboard_view(request):
    dict={
    
    'total_course':QMODEL.Speciality.objects.all().count(),
    'total_question':QMODEL.Question.objects.all().count(),
    }
    return render(request, 'participant/dashboard.html',context=dict)
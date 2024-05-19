from django.shortcuts import render, redirect
from .import forms, models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import Group

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')  
    return render(request,'index.html')

def is_participant(user):
    return user.groups.filter(name='PARTICIPANT').exists()

def is_facilitator(user):
    return user.groups.filter(name='FACILITATOR').exists()

def afterlogin_view(request):
    if is_participant(request.user):      
        return redirect('participant/dashboard')
                
    # elif is_teacher(request.user):
    #     accountapproval=TMODEL.Teacher.objects.all().filter(user_id=request.user.id,status=True)
    #     if accountapproval:
    #         return redirect('teacher/teacher-dashboard')
    #     else:
    #         return render(request,'teacher/teacher_wait_for_approval.html')
    # else:
    #     return redirect('admin-dashboard')

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


from django.shortcuts import render
from .import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from challenge import models as QMODEL
from participant import models as FMODEL
from challenge import forms as QFORM
from datetime import datetime
from django.urls import reverse
# Create your views here.


def facilitatorhome(request):
    current_time = datetime.now()
    context = {
        'current_time': current_time
    }
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'facilitator/home.html', context)

def facilitator_signup_view(request):
    userForm=forms.FacilitatorUserForm()
    facilitatorForm=forms.FacilitatorForm()
    mydict={'userForm':userForm,'facilitatorForm':facilitatorForm}
    if request.method == 'POST':
        userForm = forms.FacilitatorUserForm(request.POST)
        facilitatorForm = forms.FacilitatorForm(request.POST,request.FILES)
        if userForm.is_valid() and facilitatorForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            facilitator = facilitatorForm.save(commit=False)
            facilitator.user = user
            facilitator.save()
            my_facilitator_group = Group.objects.get_or_create(name='FACILITATOR')
            my_facilitator_group[0].user_set.add(user)
        return HttpResponseRedirect(reverse('facilitatorlogin'))
    return render(request, 'facilitator/signup.html', context=mydict)


def is_facilitator(user):
    return user.groups.filter(name='FACILITATOR').exists()

@login_required(login_url='facilitatorlogin')
@user_passes_test(is_facilitator)
def facilitator_dashboard_view(request):
    dict={
    'total_speciality':QMODEL.Speciality.objects.all().count(),
    'total_question':QMODEL.Question.objects.all().count(),
    'total_participants':FMODEL.Participant.objects.all().count()
    }
    return render(request,'facilitator/dashboard.html',context=dict)


@login_required(login_url='facilitatorlogin')
@user_passes_test(is_facilitator)
def add_or_view_challenge_view(request):
    return render(request,'facilitator/add_or_view.html')
'''
Adding challenges
'''
@login_required(login_url='facilitatorlogin')
@user_passes_test(is_facilitator)
def add_challenge_view(request):
    specilaityForm = QFORM.SpecialityForm()
    if request.method == 'POST':
        specilaityForm = QFORM.SpecialityForm(request.POST)
        if specilaityForm.is_valid():        
            specilaityForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect(reverse('viewchallenge'))
    context = {
        'specialityForm': specilaityForm
    }
    return render(request,'facilitator/add_challenge.html', context)

@login_required(login_url='facilitatorlogin')
@user_passes_test(is_facilitator)
def viewchallengeview(request):
    challenges = QMODEL.Speciality.objects.all()
    return render(request,'facilitator/challenge_view.html',{'challenges':challenges})

'''
Deleting challenges
'''
@login_required(login_url='facilitatorlogin')
@user_passes_test(is_facilitator)
def challenge_del_view(request, pk):
    challenge = QMODEL.Speciality.objects.get(id=pk)
    challenge.delete()
    return HttpResponseRedirect(reverse('viewchallenge'))
    
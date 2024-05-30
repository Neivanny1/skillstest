from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import Group
from . import forms, models
from django.contrib.auth.decorators import login_required, user_passes_test
from challenge import models as QMODEL
from datetime import datetime

'''
Home view
'''
def participanthome(request):
    current_time = datetime.now()
    context = {
        'current_time': current_time
    }
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('afterlogin'))
    return render(request, 'participant/home.html', context)

'''
Signup view
'''
def participant_signup_view(request):
    userForm = forms.ParticipantUserForm()
    participantForm = forms.ParticipantForm()
    mydict = {'userForm': userForm, 'participantForm': participantForm}

    if request.method == 'POST':
        userForm = forms.ParticipantUserForm(request.POST)
        participantForm = forms.ParticipantForm(request.POST, request.FILES)
        
        if userForm.is_valid() and participantForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            participant = participantForm.save(commit=False)
            participant.user = user
            participant.save()
            my_participant_group = Group.objects.get_or_create(name='PARTICIPANT')
            my_participant_group[0].user_set.add(user)
            return HttpResponseRedirect(reverse('participantlogin'))
    return render(request, 'participant/signup.html', context=mydict)

def is_participant(user):
    return user.groups.filter(name='PARTICIPANT').exists()
'''
Dashboard view
'''
@login_required(login_url='participantlogin')
@user_passes_test(is_participant)
def participant_dashboard_view(request):
    context = {
        'total_speciality': QMODEL.Speciality.objects.all().count(),
        'total_question': QMODEL.Question.objects.all().count(),
    }
    return render(request, 'participant/dashboard.html', context)

'''
Available challenges view
'''
@login_required(login_url='participantlogin')
@user_passes_test(is_participant)
def view_challenges_view(request):
    speciality = QMODEL.Speciality.objects.all()
    return render(request,'participant/view_challenges.html', {'speciality':speciality})

'''
Join challenge view
'''
@login_required(login_url='participantlogin')
@user_passes_test(is_participant)
def join_challenge_view(request, pk):
    speciality = QMODEL.Speciality.objects.get(id=pk)
    total_questions = QMODEL.Question.objects.all().filter(speciality=speciality).count()
    questions = QMODEL.Question.objects.all().filter(speciality=speciality)
    total_marks = 0
    for q in questions:
        total_marks = total_marks + q.marks
    return render(request,'participant/join_challenge.html',
                  {'speciality':speciality,
                   'total_questions':total_questions,
                   'total_marks':total_marks})

'''
Start challenge
'''
@login_required(login_url='participantlogin')
@user_passes_test(is_participant)
def start_challenge_view(request, pk):
    speciality = QMODEL.Speciality.objects.get(id=pk)
    questions = QMODEL.Question.objects.all().filter(speciality=speciality)
    if request.method == 'POST':
        pass
    response = render(request,
                      'participant/start_challenge.html',
                      {'speciality':speciality,
                       'questions':questions})
    response.set_cookie('speciality_id',speciality.id)
    return response

'''
Calculate marks
'''
@login_required(login_url='participantlogin')
@user_passes_test(is_participant)
def calculate_marks_view(request):
    if request.COOKIES.get('speciality_id') is not None:
        speciality_id = request.COOKIES.get('speciality_id')
        speciality = QMODEL.Speciality.objects.get(id=speciality_id)
        
        total_marks = 0
        questions = QMODEL.Question.objects.all().filter(speciality=speciality)
        for i in range(len(questions)):
            selected_ans = request.COOKIES.get(str(i+1))
            actual_answer = questions[i].answer
            if selected_ans == actual_answer:
                total_marks += questions[i].marks
        
        participant = models.Participant.objects.get(user_id=request.user.id)
        result = QMODEL.Result()
        result.marks = total_marks
        result.speciality = speciality
        result.participant = participant
        result.save()

        response = render(request, 'participant/view_result.html', {'marks': total_marks})
        response.delete_cookie('speciality_id')
        for i in range(len(questions)):
            response.delete_cookie(str(i+1))
        
        return response
    return HttpResponseRedirect(reverse('take_challenge'))

'''
View results
'''
@login_required(login_url='studentlogin')
@user_passes_test(is_participant)
def view_result_view(request):
    speciality = QMODEL.Speciality.objects.all()
    return render(request,'participant/view_result.html',{'speciality':speciality})

'''
Check Marks
'''
@login_required(login_url='participant')
@user_passes_test(is_participant)
def check_marks_view(request, pk):
    speciality = QMODEL.Speciality.objects.get(id=pk)
    participant = models.Participant.objects.get(user_id=request.user.id)
    results= QMODEL.Result.objects.all().filter(speciality=speciality ).filter(participant=participant)
    return render(request,'participant/check_marks.html',{'results':results})

'''
Participant history
'''
@login_required(login_url='participantlogin')
@user_passes_test(is_participant)
def view_history_view(request):
    speciality = QMODEL.Speciality.objects.all()
    return render(request,'participant/history.html',{'speciality':speciality})
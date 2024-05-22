from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from participant.views import is_participant
from django.contrib.auth.models import User
from django.core.mail import send_mail
from . import forms, models
from django.conf import settings
from django.urls import reverse
from facilitator.views import is_facilitator
from facilitator import models as FMODEL
from participant.views import is_participant
from participant import models as PMODEL

'''
Handles home page display
'''
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('afterlogin'))  
    return render(request,'index.html')

'''
Admin home view
'''
def admin_home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('afterlogin'))
    return HttpResponseRedirect(reverse('adminlogin'))


'''
Admin dashboard
'''
def admin_dashboard_view(request):
    dict = {
        'total_participant': PMODEL.Participant.objects.all().count(),
        'total_facilitator': FMODEL.Facilitator.objects.all().filter(status=True).count(),
        'total_speciality': models.Speciality.objects.all().count(),
        'total_question': models.Question.objects.all().count(),
    }
    return render(request, 'challenge/adminDash.html', context=dict)


'''
Handles all logins
'''
def afterlogin_view(request):
    if is_participant(request.user):
        url = reverse('participantdashboard')
        return redirect(url)
                
    elif is_facilitator(request.user):
        accountapproval = FMODEL.Facilitator.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('facilitator/dashboard')
        else:
            return render(request,'facilitator/approval.html')
    else:
        return redirect('adminhome')

'''
Handles aboout information
'''
def aboutus_view(request):
    return render(request,'about.html')

'''
Handles contact information
'''
def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'onsend.html')
    return render(request, 'contact.html', {'form':sub})
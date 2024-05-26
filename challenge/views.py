from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from participant.views import is_participant
from django.contrib.auth.models import User
from django.core.mail import send_mail
from . import forms, models
from django.conf import settings
from django.urls import reverse
from facilitator.views import is_facilitator
from facilitator import models as FMODEL
from facilitator import forms as FFORM
from participant.views import is_participant
from participant import models as PMODEL
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import messages
'''
Handles home page display
'''
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('afterlogin'))  
    return render(request,'index.html')

'''
Handles all logins
'''
def afterlogin_view(request):
    if is_participant(request.user):
        return redirect(reverse('participantdashboard'))
                
    elif is_facilitator(request.user):
        accountapproval = FMODEL.Facilitator.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect(reverse('facilitatordashboard'))
        else:
            return render(request,'facilitator/approval.html')
    elif is_admin(request.user):
        return redirect('admindash')


'''
Admin home view
'''
def admin_home_view(request):
    if request.user.is_authenticated:
        return redirect('afterlogin')
    else:
        return redirect('adminlogin')

def is_admin(user):
    return user.is_superuser
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
Displays all facilitators details
BOth approved and pending
'''
@login_required(login_url='adminlogin')
def view_facilitators_view(request):
    dict={
    'total_facilitator':FMODEL.Facilitator.objects.all().filter(status=True).count(),
    'pending_facilitator':FMODEL.Facilitator.objects.all().filter(status=False).count(),
    'salary':FMODEL.Facilitator.objects.all().filter(status=True).aggregate(Sum('salary'))['salary__sum'],
    }
    return render(request,'challenge/view_facilitators.html',context=dict)

'''
Approved facilitators
'''
@login_required(login_url='adminlogin')
def view_facilitator_view(request):
    facilitator = FMODEL.Facilitator.objects.all().filter(status=True)
    return render(request,'challenge/view_facilitator.html',{'facilitator':facilitator})
'''
Check any pending approvals
'''
@login_required(login_url='adminlogin')
def check_pending_approval_view(request):
    pending_accounts = FMODEL.Facilitator.objects.all().filter(status=False)
    context = {
        'pending_accounts': pending_accounts
    }
    return render(request, 'challenge/pending_approval.html', context)


'''
Handles approving pending aprovals
'''
@login_required(login_url='adminlogin')
def approve_pending_view(request, pk):
    f_pay = forms.FacilitatorPayForm()
    if request.method == 'POST':
        f_pay = forms.FacilitatorPayForm(request.POST)
        if f_pay.is_valid():
            f = FMODEL.Facilitator.objects.get(id=pk)
            f.salary = f_pay.cleaned_data['salary']
            f.status = True
            f.save()
        else:
            messages.warning(request, ('Please fill all the fields'))
        return HttpResponseRedirect(reverse('checkpending'))
    context = {
        'f_pay': f_pay
        }
    messages.success(request, ('Facilitator Approved Sucessfully'))
    return render(request, 'challenge/payout.html', context)

'''
Rejecting approvals
'''
@login_required(login_url='adminlogin')
def reject_pending_view(request, pk):
    facilitator = FMODEL.Facilitator.objects.get(id=pk)
    user = User.objects.get(id=facilitator.user_id)
    user.delete()
    facilitator.delete()
    messages.success(request, ('Facilitator Rejected Sucessfully'))
    return HttpResponseRedirect(reverse('checkpending'))

'''
Updating facilitators details
'''
@login_required(login_url='adminlogin')
def update_facilitator_view(request,pk):
    facilitator = FMODEL.Facilitator.objects.get(id=pk)
    user = FMODEL.User.objects.get(id=facilitator.user_id)
    userForm = FFORM.FacilitatorUserForm(instance=user)
    facilitatorForm = FFORM.FacilitatorForm(request.FILES,instance=facilitator)
    mydict={'userForm':userForm,'facilitatorForm':facilitatorForm}
    if request.method == 'POST':
        userForm = FFORM.FacilitatorUserForm(request.POST,instance=user)
        facilitatorForm = FFORM.FacilitatorForm(request.POST,request.FILES,instance=facilitator)
        if userForm.is_valid() and facilitatorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            facilitatorForm.save()
            messages.success(request, ('Facilitator Updated Sucessfully'))
            return redirect(reverse('viewfacilitator'))
    return render(request,'challenge/update_facilitator.html', context=mydict)
'''
Checking Total payouts
'''
@login_required(login_url='adminlogin')
def total_payout_view(request):
    facilitators = FMODEL.Facilitator.objects.all().filter(status=True)
    return render(request,'challenge/total_payout.html',{'facilitators':facilitators})

'''
Deleting Facilitator
'''
@login_required(login_url='adminlogin')
def delete_facilitator_view(request,pk):
    facilitator = FMODEL.Facilitator.objects.get(id=pk)
    user =User.objects.get(id=facilitator.user_id)
    user.delete()
    facilitator.delete()
    messages.success(request, ('Facilitator Deleted Sucessfully'))
    return HttpResponseRedirect(reverse('viewfacilitator'))


'''
Handles aboout information
'''
def aboutus_view(request):
    return render(request,'aboutus.html')


'''
Handles contact information
'''
# def contactus_view(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         sender_email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
        
#         if name and sender_email and subject and message:
#             full_message = f"Name: {name}\n Email: {sender_email}\n\nMessage:\n{message}"
#             try:
#                 send_mail(subject,
#                           full_message,
#                           sender_email,
#                           [settings.EMAIL_HOST_USER],
#                           fail_silently=False)
#                 return render(request, 'onsucess.html')
#             except Exception as e:
#                 return render(request, 'onfail.html')
#     return render(request, 'contact.html')

def contactus_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            try:
                send_mail(subject,
                          full_message,
                          email,
                          [settings.EMAIL_HOST_USER],
                          fail_silently=False)
                return render(request, 'onsend.html')
            except Exception as e:
                return HttpResponse(f'An error occurred: {e}')
        else:
            return HttpResponse('All fields are required.')
    return render(request, 'contact.html')
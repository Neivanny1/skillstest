from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from participant.views import is_participant
from django.contrib.auth.models import User
# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')  
    return render(request,'index.html')


def afterlogin_view(request):
    if is_participant(request.user):      
        return redirect('participant/participantdashboard')
                
    # elif is_teacher(request.user):
    #     accountapproval=TMODEL.Teacher.objects.all().filter(user_id=request.user.id,status=True)
    #     if accountapproval:
    #         return redirect('teacher/teacher-dashboard')
    #     else:
    #         return render(request,'teacher/teacher_wait_for_approval.html')
    # else:
    #     return redirect('admin-dashboard')

def aboutus_view(request):
    return render(request,'aboutus.html')
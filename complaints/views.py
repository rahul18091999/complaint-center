from django.shortcuts import render,redirect
from user_login.models import complaints
from .form import *
from django.contrib.auth.decorators import login_required
from workers.models import workers
from complaints.models import Department
from django.core.mail import send_mail
from workers.models import workers,workerType

# Create your views here.
@login_required(login_url="/user_login/home")
def login(request):
    wor=workerType.objects.all()
    dep=Department.objects.all()
    if request.method == 'POST':
            subject=request.POST.get("subject")
            department=request.POST.get("department")
            roomno=request.POST.get("roomno")
            comp_type=request.POST.get("types")
            description=request.POST.get("description")
            username=request.user
            comp=complaints(subject=subject,department=department,roomno=roomno,problem_type=comp_type,description=description,name=username)
            comp.save()
            # wor=workers.objects.filter(worker_typer=comp_type)
            # wor_email=wor.worker_email
            # send_mail(subject=subject,
            # message=description,
            # from_email="harshrawal8295@gmail.com",
            # recipient_list=[wor_email])
    return render(request, 'complaint_page.html',{'wor':wor, 'dep':dep})
# @login_required(login_url="/user_login/home")
# def save_complaints(request):
    
#             return redirect("/user_login/logout")
from django.shortcuts import render,redirect
from .models import *
from .forms import pendinggg
from django.http import HttpResponse
from user_login.models import complaints
from django.contrib.auth.decorators import login_required

# Create your views here.
#   show worker
@login_required(login_url="/user_login/home")
def workerlogin(request):
    try:
        username=request.user
        worker_table=workers.objects.get(username=username)
        typ=worker_table.worker_typer
        print(typ)
        comp=list(complaints.objects.filter(problem_type=typ,complaint_status="pending"))
        compa=list(complaints.objects.filter(problem_type=typ,complaint_status="approved"))
        compc=list(complaints.objects.filter(problem_type=typ,complaint_status="completed"))
        return render(request,'view-complaint.html',{"comp": comp,"compa":compa,"compc":compc})
    except:
        return HttpResponse("<h2>you are not registerd as workers</h2>")
#    change status
@login_required(login_url="/user_login/home")
def pending(request,id):
    if request.method == "POST":
        pend = pendinggg(request.POST)
        if pend.is_valid:
            pen=pend.data.get("pending")
            if pen == "approved":
                comp=complaints.objects.get(id=id)
                comp.complaint_status="approved"
                comp.save()
                return redirect("/worker_login/workerlogin")
            elif pen == "completed":
                comp=complaints.objects.get(id=id)
                comp.complaint_status="completed"
                comp.save()
                return redirect("/worker_login/workerlogin")
            else:
                return redirect("/worker_login/workerlogin")
        else:
            return redirect("/worker_login/workerlogin")
    else:
        return redirect("/worker_login/workerlogin")
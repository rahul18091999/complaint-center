from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import dep,work,user
from django.contrib.auth.models import auth,User
from complaints.models import Department
from django.contrib.auth.decorators import login_required
from admins.forms import work
from workers.models import workers,workerType
from django.contrib import messages
from user_login.models import subscriber
# Create your views here.
@login_required(login_url="/user_login/home")
def adminreq(request):
    if request.user.is_superuser:
        return render(request, "admin/adddepartment.html")
    else:
        return HttpResponse("<h1>You are not authorized to this page</h1>")


@login_required(login_url="/user_login/home")
def addDepartment(request):
        if request.method == "POST":
            
                hod_name=request.POST.get("dep_hod")
                hod_dep=request.POST.get("dep_name")
                hod_use=request.POST.get("hod_username")
                hod_mail=request.POST.get("hod_email")
                hod_phno=request.POST.get("hod_ph")
                hod_pass=request.POST.get("hod_password")

                try:
                    use=User.objects.get(username=hod_use)                
                    messages.error(request,'UserName must be unique')
                    return render(request,"admin/addDepartment.html")
                    # 
                except:          
                    pass
                try:
                    depa=Department.objects.get(Department_name=hod_dep)
                    messages.error(request,'Department Name must be unique')
                    return render(request,"admin/addDepartment.html")
                except:
                    pass
                use=User.objects.create_user(username=hod_use,password=hod_pass,email=hod_mail)                
                depa=Department(Department_name=hod_dep,HOD_name=hod_name,HOD_username=hod_use,HOD_email=hod_mail,HOD_phno=hod_phno)

                depa.save()
                use.save()
                messages.success(request,"Department added Successfully")
                return render(request,'admin/addDepartment.html')
        else:
            return render(request,"admin/addDepartment.html")
@login_required(login_url="/user_login/home")
def addWorker(request):
        work = workerType.objects.all()
        if request.method == "POST":
                typ=request.POST.get("types")
                usern=request.POST.get("username")
                first=request.POST.get("first_name")
                last=request.POST.get("last_name")
                mail=request.POST.get("email")
                ph=request.POST.get("worker_ph")
                pw=request.POST.get("password")
                try:
                    use=User.objects.get(username=usern)                
                    messages.error(request,'UserName must be unique')
                    return render(request,"admin/addWorker.html",{'worker':work})
                    
                except:          
                    pass
                use=User.objects.create_user(username=usern,password=pw,email=mail)                
                wor=workers(username=usern,first_name=first,last_name=last,worker_email=mail,worker_phno=ph,worker_typer=typ)
                wor.save()
                messages.success(request,"Worker added Successfully")
                return render(request,'admin/addWorker.html',{'worker':work})
        else:
            return render(request,"admin/addWorker.html",{'worker':work})
@login_required(login_url="/user_login/home")
def addUser(request):
        if request.method == "POST":
                usern=request.POST.get("user_username")
                first=request.POST.get("first_name")
                last=request.POST.get("last_name")
                mail=request.POST.get("user_email")
                ph=request.POST.get("user_ph")
                pw=request.POST.get("user_pass")
                try:
                    use=User.objects.get(username=usern)                
                    messages.error(request,'UserName must be unique')
                    return render(request,"admin/adduser.html")
                    
                except:          
                    pass
                use=User.objects.create_user(username=usern,password=pw,email=mail)  
                use.save()              
                sub=subscriber(rollno=usern,first_name=first,last_name=last,email=mail,phno=ph,user_name=usern)
                sub.save()
                messages.success(request,"User added Successfully")
                return redirect('/adminpanel/addUser')
        else:
            return render(request,"admin/adduser.html")
            
@login_required(login_url="/user_login/home")
def showDepartment(request):
    department = list(Department.objects.all())
    return render(request,'admin/showDepartment.html',{'department':department})

login_required(login_url="/user_login/home")
def deleteDepartment(request):
    idd = request.GET.get('id')
    data = Department.objects.get(HOD_username=idd)
    user = User.objects.get(username=idd).delete()
    data.delete()
    return redirect('/adminpanel/showDepartment')

@login_required(login_url="/user_login/home")
def showWorker(request):
    worker = list(workers.objects.all())
    return render(request,'admin/showworker.html',{'worker':worker})

login_required(login_url="/user_login/home")
def deleteWorker(request):
    idd = request.GET.get('id')
    data = workers.objects.get(username=idd)
    user = User.objects.get(username=idd).delete()
    data.delete()
    return redirect('/adminpanel/showWorker')


@login_required(login_url="/user_login/home")
def showUser(request):
    worker = list(subscriber.objects.all())
    print(worker)
    return render(request,'admin/showuser.html',{'suscriber':worker})

login_required(login_url="/user_login/home")
def deleteUser(request):
    idd = request.GET.get('id')
    data = subscriber.objects.get(user_name=idd)
    user = User.objects.get(username=idd).delete()
    data.delete()
    return redirect('/adminpanel/showUser')

def addWorkerType(request):
    if request.method == "POST":
        typee=request.POST.get("Type")
        try:
            workerType.objects.get(type=typee)
            messages.error(request,'Already Exists')
            return render(request,"admin/addWorkerType.html")
        except:
            wor = workerType(type=typee)
            wor.save()
            messages.success(request,'Worker type Added successfully.')
    return render(request,'./admin/addWorkerType.html')


def showWorkerType(request):
    work = workerType.objects.all()
    return render(request,'./admin/showWorkerType.html',{'worker':work})

def editDepartment(request):
    idd=request.GET.get('id')
    data = Department.objects.get(HOD_username=idd)
    print(data.Department_name)
    if request.method=="POST":
        data = Department.objects.get(HOD_username=idd)
        data.HOD_name=request.POST.get('dep_hod')
        data.HOD_email=request.POST.get('hod_email')
        data.HOD_phno=request.POST.get('hod_ph')
        data.save()
        return redirect('/adminpanel/showDepartment')
    return render(request,'./admin/editdepartment.html',{'data':data})

def editWorker(request):
    idd=request.GET.get('id')
    data = workers.objects.get(username=idd)
    work = workerType.objects.all()
    if request.method=="POST":
        data = workers.objects.get(username=idd)
        data.worker_phno=request.POST.get('worker_ph')
        data.worker_typer=request.POST.get('types')
        data.worker_email=request.POST.get('email')
        data.first_name=request.POST.get('first_name')
        data.last_name=request.POST.get('last_name')
        data.save()
        return redirect('/adminpanel/showWorker')
    return render(request,'./admin/editworker.html',{'data':data,'worker':work})

def editUser(request):
    idd=request.GET.get('id')
    data = subscriber.objects.get(user_name=idd)
    if request.method=="POST":
        data = subscriber.objects.get(user_name=idd)
        data.first_name=request.POST.get("first_name")
        data.last_name=request.POST.get("last_name")
        data.email=request.POST.get("user_email")
        data.phno=request.POST.get("user_ph")
        data.save()
        return redirect('/adminpanel/showUser')
    return render(request,'./admin/edituser.html',{'data':data})

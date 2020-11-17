from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth,models
from workers.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def login(request):
    if request.method == "POST":
            usern=request.POST.get("uid")
            userp=request.POST.get("pid")
            login_user=auth.authenticate(username=usern,password=userp)         #user login authenticate
            if login_user is not None:
                auth.login(request, login_user)                     #logged in
                
                if request.user.is_superuser:
                    request.session['type']="admin" 
                    request.session['username']=usern                  #admin
                    return redirect('/adminpanel/addDepartment')            
                else:
                    try:                                        #worker
                        wor=workers.objects.get(username=usern)
                        request.session['type']="worker"                
                        request.session['username']=usern
                        return redirect('/worker_login/workerlogin')
                    except:                            
                        request.session['type']="user"                  
                        request.session['username']=usern
                        return redirect('/complaints/log')
            

            else:
                messages.error(request,'username or password not correct')
                return redirect('/')
    else:
        return render(request,"Login.html")
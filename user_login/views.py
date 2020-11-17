from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth,models
from .forms import *
from workers.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def home(request):                              #home page
    return render(request,"Login.html")

def logedin(request):                           #user login
        if request.method == "POST":
            user_log = userlogin(request.POST)      #form
            if user_log.is_valid:
                usern=user_log.data.get("uid")
                userp=user_log.data.get("pid")
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
                    return redirect('/user_login/home')
            
            else:
                return redirect('/user_login/home')
        else:
            return redirect('/user_login/home')
# logout
@login_required(login_url="/user_login/home")
def logout(request):
    try:
        auth.logout(request)
        del request.session['type']
        del request.session['username']
        return redirect('/')
    except:
        return redirect('/')
        

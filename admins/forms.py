from django import forms

class dep(forms.Form):
    dep_hod=forms.CharField(max_length=50)
    dep_name=forms.CharField(max_length=10)
    hod_username=forms.CharField(max_length="50")
    hod_email=forms.EmailField()
    hod_ph=forms.IntegerField()
    hod_password=forms.PasswordInput()

class work(forms.Form):
    types=forms.CharField( max_length=20)
    username=forms.CharField( max_length=50)
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    email=forms.EmailField()
    worker_ph=forms.IntegerField()
    password=forms.PasswordInput()

class user(forms.Form):
    user_username=forms.CharField(max_length=25)
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    user_email=forms.EmailField()
    user_ph=forms.IntegerField()
    user_pass=forms.PasswordInput()
    
from django import forms


class userlogin(forms.Form):
    uid=forms.CharField(max_length=25)
    pid=forms.PasswordInput()
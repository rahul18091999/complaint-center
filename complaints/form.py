from django import forms

class save_comp(forms.Form):
    subject=forms.CharField(max_length=50)
    department=forms.CharField(max_length=50)
    roomno=forms.CharField(max_length=10)
    types=forms.CharField(max_length=50)
    description=forms.TextInput()
    

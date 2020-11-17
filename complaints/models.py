from django.db import models

# Create your models here.

class Department(models.Model):
    Department_name=models.CharField(max_length=20,unique=True)
    HOD_username=models.CharField(max_length=50)
    HOD_name=models.CharField(max_length=50)
    HOD_email=models.EmailField()
    HOD_phno=models.IntegerField() 
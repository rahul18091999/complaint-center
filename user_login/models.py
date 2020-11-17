from django.db import models

# Create your models here.
class complaints(models.Model):                 #complaint table
    name=models.CharField(max_length=50)
    problem_type=models.TextField()
    department=models.CharField(max_length=50)
    roomno=models.IntegerField()
    subject=models.CharField(max_length=50)
    description=models.TextField()
    complaint_status=models.CharField(max_length=50, default="pending")


class subscriber(models.Model):
    rollno=models.CharField(max_length=20)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    phno=models.IntegerField()
    user_name = models.CharField(max_length=50)
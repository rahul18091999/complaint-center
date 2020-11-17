from django.db import models

# Create your models here.
class workers(models.Model):                #worker tabe
    username=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    worker_email=models.EmailField()
    worker_phno=models.IntegerField()
    worker_typer=models.CharField(max_length=50)

class workerType(models.Model):
    type = models.CharField(max_length = 50,unique=True)
from django.urls import path,include
from .views import *

urlpatterns = [
    path("workerlogin",workerlogin),
    path("pending/<id>",pending),
    
]

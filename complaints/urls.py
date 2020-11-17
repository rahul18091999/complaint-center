from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    # path("complaint_submit",save_complaints),
    path('log',login),
]

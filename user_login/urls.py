from django.urls import path
from .views import *
urlpatterns = [
    path('home',home),
    path('login',logedin),
    path('logout',logout),


]

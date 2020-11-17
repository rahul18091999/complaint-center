from django.urls import path
from .views import *
urlpatterns = [
    path('admin',adminreq),
    path('addDepartment',addDepartment),
    path('addWorker',addWorker),
    path('addUser',addUser),
    path('showDepartment',showDepartment),
    path('showWorker',showWorker),
    path('showUser',showUser),
    path('deleteDepartment',deleteDepartment),
    path('deleteWorker',deleteWorker),
    path('deleteUser',deleteUser),
    path('addWorkerType',addWorkerType),
    path('showWorkerType',showWorkerType),
    path('editDepartment',editDepartment),
    path('editWorker',editWorker),
    path('editUser',editUser),
]